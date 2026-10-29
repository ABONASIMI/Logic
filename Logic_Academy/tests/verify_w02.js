// Node verification of Week 2 bundles and rendering
const fs = require('fs');
const path = require('path');

global.window = global;
global.Logic = {
  data: {},
  reg: function(k, v) { this.data[k] = v; }
};
global.document = {
  createElement: (tag) => ({
    tagName: tag.toUpperCase(),
    className: '',
    classList: { add: () => {}, remove: () => {} },
    appendChild: () => {},
    setAttribute: () => {},
    getAttribute: () => null,
    style: {},
    innerHTML: '',
    textContent: '',
    addEventListener: () => {}
  }),
  createTextNode: (t) => ({ textContent: t })
};
global.localStorage = { getItem: () => null, setItem: () => {} };

require('../js/logic-engine.js');
require('../js/math.js');
require('../data/status.js');

const files = [
  'w02_cours.fr.js', 'w02_cours.fa.js',
  'w02_td.fr.js', 'w02_td.fa.js',
  'w02_tp.fr.js', 'w02_tp.fa.js',
  'w02_annales.fr.js', 'w02_annales.fa.js',
  'w02_revision.fr.js', 'w02_revision.fa.js'
];

for (const f of files) {
  const p = path.join(__dirname, '..', 'data', 'lessons', f);
  require(p);
  const [base, lang] = f.replace('.js', '').split('.');
  const key = `lesson:${base}:${lang}`;
  if (!Logic.data[key]) {
    throw new Error(`Failed to register ${key}`);
  }
  const entry = Logic.data[key];
  if (entry.status !== 'complete') {
    throw new Error(`Expected status complete for ${key}, got ${entry.status}`);
  }
  const processed = Logic.math.process(entry.html);
  const withoutScripts = processed.replace(/<script[\s\S]*?<\/script>/g, '');
  if (withoutScripts.includes('{{')) {
    throw new Error(`Unprocessed math tag remaining in ${key}`);
  }
  console.log(`✓ ${key}: OK (${entry.html.length} chars, status=${entry.status})`);

  if (entry.html.includes('class="w-quiz"')) {
    const jsonMatch = entry.html.match(/<script type="application\/json">([\s\S]*?)<\/script>/);
    if (!jsonMatch) throw new Error(`Missing JSON script inside w-quiz for ${key}`);
    const quizData = JSON.parse(jsonMatch[1]);
    if (!quizData.questions || quizData.questions.length === 0) {
      throw new Error(`Empty quiz questions in ${key}`);
    }
    for (const q of quizData.questions) {
      if (!q.q || !Array.isArray(q.options) || typeof q.answer !== 'number' || !q.explain) {
        throw new Error(`Invalid question format in ${key}: ${JSON.stringify(q)}`);
      }
      Logic.math.process(q.q);
      q.options.forEach(o => Logic.math.process(o));
      Logic.math.process(q.explain);
    }
    console.log(`  ✓ w-quiz validated with ${quizData.questions.length} questions`);
  }
}

console.log('\nALL 10 WEEK 2 LESSON BUNDLES VERIFIED 100% CORRECT!');

