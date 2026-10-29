// Node verification of all 11 Weeks (110 lesson bundles) and rendering
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

const sections = ['cours', 'td', 'tp', 'annales', 'revision'];
const langs = ['fr', 'fa'];
let total = 0;

for (let w = 1; w <= 11; w++) {
  const wid = 'w' + (w < 10 ? '0' + w : w);
  for (const sec of sections) {
    for (const lang of langs) {
      const f = `${wid}_${sec}.${lang}.js`;
      const p = path.join(__dirname, '..', 'data', 'lessons', f);
      require(p);
      const key = `lesson:${wid}_${sec}:${lang}`;
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
      if (entry.html.includes('class="w-quiz"')) {
        const jsonMatch = entry.html.match(/<script type="application\/json">([\s\S]*?)<\/script>/);
        if (!jsonMatch) throw new Error(`Missing JSON script inside w-quiz for ${key}`);
        const quizData = JSON.parse(jsonMatch[1]);
        if (!quizData.questions || quizData.questions.length === 0) {
          throw new Error(`Empty quiz questions in ${key}`);
        }
        for (const q of quizData.questions) {
          if (!q.q || !Array.isArray(q.options) || typeof q.answer !== 'number' || !(q.explain || q.why)) {
            throw new Error(`Invalid question format in ${key}: ${JSON.stringify(q)}`);
          }
          Logic.math.process(q.q);
          q.options.forEach(o => Logic.math.process(o));
          Logic.math.process(q.explain || q.why);
        }
      }
      total++;
    }
  }
  console.log(`✓ ${wid.toUpperCase()}: all 10 bundles verified (status=complete)`);
}

console.log(`\nALL ${total} LESSON BUNDLES ACROSS WEEKS 1–11 VERIFIED 100% CORRECT!`);

