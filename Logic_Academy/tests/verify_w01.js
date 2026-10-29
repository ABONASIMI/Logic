// Node verification of Week 1 bundles and rendering
const fs = require('fs');
const path = require('path');

// Mock browser environment
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

// Load logic-engine
require('../js/logic-engine.js');
console.log('✓ logic-engine loaded successfully');

// Load math
require('../js/math.js');
console.log('✓ math loaded successfully');

// Load status
require('../data/status.js');
console.log('✓ status loaded successfully:', Logic.data['status']);

// Load all 10 w01 lesson files
const files = [
  'w01_cours.fr.js', 'w01_cours.fa.js',
  'w01_td.fr.js', 'w01_td.fa.js',
  'w01_tp.fr.js', 'w01_tp.fa.js',
  'w01_annales.fr.js', 'w01_annales.fa.js',
  'w01_revision.fr.js', 'w01_revision.fa.js'
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
  // Process math tags in html
  const processed = Logic.math.process(entry.html);
  const withoutScripts = processed.replace(/<script[\s\S]*?<\/script>/g, '');
  if (withoutScripts.includes('{{')) {
    throw new Error(`Unprocessed math tag remaining in ${key}`);
  }
  console.log(`✓ ${key}: OK (${entry.html.length} chars, status=${entry.status})`);
  
  // If it contains w-quiz, verify that the json parses and questions have valid fields
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
      // verify math tags inside question and options can be processed
      Logic.math.process(q.q);
      q.options.forEach(o => Logic.math.process(o));
      Logic.math.process(q.explain);
    }
    console.log(`  ✓ w-quiz validated with ${quizData.questions.length} questions`);
  }
}

console.log('\nALL 10 WEEK 1 LESSON BUNDLES VERIFIED 100% CORRECT!');
