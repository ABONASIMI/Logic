/* Logic Academy - Interactive Logic Engines (Truth Tables, AST, NatDed Fitch, DPLL, Steppers) */
(function () {
  'use strict';
  var LogicTools = (window.LogicTools = window.LogicTools || {});

  // ---------------------------------------------------------------------------------------------- 1. Exercise Stepper
  /**
   * Initializes an interactive stepper inside containerEl
   * @param {HTMLElement} containerEl 
   * @param {Object} data { id, title, statement, consigne, hint, steps, finalAnswer, justification, verification, trap, lang }
   */
  LogicTools.renderExerciseStepper = function (containerEl, data) {
    if (!containerEl) return;
    var lang = data.lang || 'fr';
    var isFa = lang === 'fa';

    var uiText = {
      tryDraft: isFa ? 'پیش‌نویس پاسخ خود را اینجا بنویسید (اختیاری)...' : 'Rédigez votre essai ou réponse ici (brouillon)...',
      hintBtn: isFa ? '💡 راهنمایی' : '💡 Indice',
      nextStepBtn: isFa ? '▶ مرحله بعد' : '▶ Étape suivante',
      fullSolBtn: isFa ? '👁 حل کامل' : '👁 Solution complète',
      hideBtn: isFa ? '✖ بستن راه‌حل' : '✖ Masquer la solution',
      consigneTitle: isFa ? 'فهمیدن خواست سؤال (در آزمون سوربن چه انتظاری می‌رود؟)' : 'Comprendre la consigne (Attentes à l\'examen)',
      trapTitle: isFa ? 'چرا اشتباه می‌کنم؟ (دام‌های رایج و تحلیل خطا)' : 'Pourquoi je me trompe ? (Pièges fréquents)',
      verifTitle: isFa ? 'چگونه درستی پاسخ را بررسی کنیم؟' : 'Comment vérifier la réponse ?',
      stepPrefix: isFa ? 'مرحله' : 'Étape',
      finalTitle: isFa ? 'پاسخ نهایی رسمی سوربن' : 'Réponse finale conforme Sorbonne',
      markDone: isFa ? 'ثبت به عنوان حل‌شده' : 'Marquer comme résolu',
      markUndone: isFa ? 'لغو وضعیت حل‌شده' : 'Marquer comme non résolu'
    };

    var currentStep = 0;
    var totalSteps = (data.steps && data.steps.length) || 0;
    var showFull = false;
    var showHint = false;

    function render() {
      containerEl.innerHTML = '';

      var card = document.createElement('div');
      card.className = 'exo-card';

      // Header
      var header = document.createElement('div');
      header.className = 'exo-header';
      var title = document.createElement('h3');
      title.className = 'exo-title';
      title.textContent = data.title;
      header.appendChild(title);

      var badges = document.createElement('div');
      badges.className = 'exo-meta-badges';
      if (data.source) {
        var bSrc = document.createElement('span');
        bSrc.className = 'badge';
        bSrc.textContent = '📄 ' + data.source;
        badges.appendChild(bSrc);
      }
      if (data.theme) {
        var bTh = document.createElement('span');
        bTh.className = 'badge badge-accent';
        bTh.textContent = data.theme;
        badges.appendChild(bTh);
      }
      header.appendChild(badges);
      card.appendChild(header);

      // Statement
      var stmt = document.createElement('div');
      stmt.className = 'exo-statement';
      stmt.innerHTML = data.statement;
      card.appendChild(stmt);

      // Consigne Box
      if (data.consigne) {
        var consBox = document.createElement('div');
        consBox.className = 'box-consigne';
        var consHead = document.createElement('div');
        consHead.className = 'consigne-header';
        consHead.textContent = '🎯 ' + uiText.consigneTitle;
        consBox.appendChild(consHead);
        var consContent = document.createElement('div');
        consContent.innerHTML = data.consigne;
        consBox.appendChild(consContent);
        card.appendChild(consBox);
      }

      // Draft area
      var draftWrap = document.createElement('div');
      draftWrap.style.margin = '1rem 0';
      var draftArea = document.createElement('textarea');
      draftArea.style.width = '100%';
      draftArea.style.minHeight = '70px';
      draftArea.style.padding = '8px';
      draftArea.style.borderRadius = '5px';
      draftArea.style.border = '1px dashed var(--rule-strong)';
      draftArea.style.background = 'var(--code-bg)';
      draftArea.style.color = 'var(--text)';
      draftArea.placeholder = uiText.tryDraft;
      // Load saved draft
      var draftKey = 'logic_draft_' + data.id;
      try { draftArea.value = localStorage.getItem(draftKey) || ''; } catch(e){}
      draftArea.addEventListener('input', function() {
        try { localStorage.setItem(draftKey, draftArea.value); } catch(e){}
      });
      draftWrap.appendChild(draftArea);
      card.appendChild(draftWrap);

      // Buttons
      var actions = document.createElement('div');
      actions.className = 'stepper-actions';

      if (data.hint) {
        var btnH = document.createElement('button');
        btnH.className = 'btn-step';
        btnH.textContent = uiText.hintBtn;
        btnH.onclick = function () { showHint = !showHint; render(); };
        actions.appendChild(btnH);
      }

      if (totalSteps > 0 && !showFull) {
        var btnNext = document.createElement('button');
        btnNext.className = 'btn-step btn-step-primary';
        btnNext.textContent = uiText.nextStepBtn + (currentStep < totalSteps ? ' (' + (currentStep + 1) + '/' + totalSteps + ')' : '');
        btnNext.onclick = function () {
          if (currentStep < totalSteps) currentStep++;
          else showFull = true;
          render();
        };
        actions.appendChild(btnNext);
      }

      var btnFull = document.createElement('button');
      btnFull.className = 'btn-step' + (showFull ? '' : ' btn-step-primary');
      btnFull.textContent = showFull ? uiText.hideBtn : uiText.fullSolBtn;
      btnFull.onclick = function () {
        showFull = !showFull;
        if (showFull) currentStep = totalSteps;
        render();
      };
      actions.appendChild(btnFull);

      card.appendChild(actions);

      // Hint Display
      if (showHint && data.hint) {
        var hintDiv = document.createElement('div');
        hintDiv.className = 'step-content';
        hintDiv.style.borderLeftColor = '#f57c00';
        hintDiv.innerHTML = '<strong>' + (isFa ? 'راهنمایی کلیدی:' : 'Indice clé :') + '</strong> ' + data.hint;
        card.appendChild(hintDiv);
      }

      // Step-by-Step Display
      if (currentStep > 0 && data.steps) {
        var stepsWrap = document.createElement('div');
        for (var i = 0; i < currentStep; i++) {
          var stepEl = document.createElement('div');
          stepEl.className = 'step-content';
          stepEl.innerHTML = '<strong>' + uiText.stepPrefix + ' ' + (i + 1) + ':</strong> ' + data.steps[i];
          stepsWrap.appendChild(stepEl);
        }
        card.appendChild(stepsWrap);
      }

      // Full Solution Display
      if (showFull) {
        var fullSolWrap = document.createElement('div');
        fullSolWrap.style.marginTop = '1.2rem';

        if (data.justification) {
          var justDiv = document.createElement('div');
          justDiv.className = 'step-content';
          justDiv.innerHTML = '<strong>' + (isFa ? 'توجیه ریاضی و قواعد منطقی:' : 'Justification mathématique :') + '</strong> ' + data.justification;
          fullSolWrap.appendChild(justDiv);
        }

        if (data.finalAnswer) {
          var ansDiv = document.createElement('div');
          ansDiv.className = 'step-content';
          ansDiv.style.borderLeftColor = 'var(--ok)';
          ansDiv.innerHTML = '<strong>' + uiText.finalTitle + ' :</strong><br>' + data.finalAnswer;
          fullSolWrap.appendChild(ansDiv);
        }

        if (data.verification) {
          var verifDiv = document.createElement('div');
          verifDiv.className = 'step-content';
          verifDiv.style.borderLeftColor = '#00897b';
          verifDiv.innerHTML = '<strong>' + uiText.verifTitle + '</strong><br>' + data.verification;
          fullSolWrap.appendChild(verifDiv);
        }

        if (data.trap) {
          var trapBox = document.createElement('div');
          trapBox.className = 'box-pourquoi';
          trapBox.innerHTML = '<div class="pourquoi-header">⚠️ ' + uiText.trapTitle + '</div>' + data.trap;
          fullSolWrap.appendChild(trapBox);
        }

        card.appendChild(fullSolWrap);
      }

      containerEl.appendChild(card);
    }

    render();
  };

  // ---------------------------------------------------------------------------------------------- 2. Truth Table Generator
  /**
   * Generates an interactive truth table
   * @param {string[]} variables ['p', 'q', 'r']
   * @param {Object[]} formulas [{ label: 'p => q', fn: function(v){ return (!v.p || v.q); } }]
   */
  LogicTools.renderTruthTable = function (containerEl, variables, formulas, isFa) {
    if (!containerEl) return;
    var n = variables.length;
    var totalRows = 1 << n;

    var wrap = document.createElement('div');
    wrap.className = 'truth-table-tool';

    var title = document.createElement('h4');
    title.style.margin = '0 0 0.8rem 0';
    title.textContent = isFa ? '📊 جدول درستی تعاملی' : '📊 Table de vérité interactive';
    wrap.appendChild(title);

    var table = document.createElement('table');
    table.className = 'truth-table';

    var thead = document.createElement('thead');
    var trH = document.createElement('tr');
    variables.forEach(function (v) {
      var th = document.createElement('th');
      th.textContent = v;
      trH.appendChild(th);
    });
    formulas.forEach(function (f) {
      var th = document.createElement('th');
      th.textContent = f.label;
      trH.appendChild(th);
    });
    thead.appendChild(trH);
    table.appendChild(thead);

    var tbody = document.createElement('tbody');
    var trueCounts = formulas.map(function () { return 0; });

    for (var i = 0; i < totalRows; i++) {
      var tr = document.createElement('tr');
      var val = {};
      for (var j = 0; j < n; j++) {
        var bit = (i >> (n - 1 - j)) & 1;
        val[variables[j]] = (bit === 1);
        var td = document.createElement('td');
        td.textContent = bit;
        td.style.fontWeight = '600';
        tr.appendChild(td);
      }

      formulas.forEach(function (f, fIdx) {
        var res = f.fn(val);
        if (res) trueCounts[fIdx]++;
        var td = document.createElement('td');
        td.textContent = res ? '1' : '0';
        td.className = res ? 'truth-val-true' : 'truth-val-false';
        tr.appendChild(td);
      });
      tbody.appendChild(tr);
    }
    table.appendChild(tbody);
    wrap.appendChild(table);

    // Summary of properties
    var summary = document.createElement('div');
    summary.className = 'tt-summary';
    formulas.forEach(function (f, fIdx) {
      var c = trueCounts[fIdx];
      var status = '';
      if (c === totalRows) status = isFa ? 'تاتولوژی (معتبر)' : 'Tautologie (Valide)';
      else if (c === 0) status = isFa ? 'تناقض (ناپذیرفتنی)' : 'Antilogie (Insatisfiable)';
      else status = isFa ? 'پذیرفتنی (اما نامعتبر)' : 'Satisfiable mais non valide (' + c + '/' + totalRows + ' modèles)';
      
      var sItem = document.createElement('div');
      sItem.innerHTML = '<strong>' + f.label + ' :</strong> ' + status;
      summary.appendChild(sItem);
    });
    wrap.appendChild(summary);

    containerEl.appendChild(wrap);
  };

  // ---------------------------------------------------------------------------------------------- 3. Fitch Proof Tutor
  /**
   * Renders a Natural Deduction Fitch Proof
   * @param {HTMLElement} containerEl 
   * @param {Object[]} lines [{ num: 1, text: 'p & q', rule: 'Hypothèse', boxStart: false, boxEnd: false, isHyp: true }]
   */
  LogicTools.renderFitchProof = function (containerEl, lines, isFa) {
    if (!containerEl) return;
    var proofDiv = document.createElement('div');
    proofDiv.className = 'fitch-proof';

    var currentBoxLevel = 0;
    var activeBoxes = [];

    lines.forEach(function (l) {
      var row = document.createElement('div');
      row.className = 'fitch-line';
      if (l.isHyp) row.classList.add('fitch-hyp');

      var numEl = document.createElement('div');
      numEl.className = 'fitch-num';
      numEl.textContent = l.num + '.';
      row.appendChild(numEl);

      var formulaEl = document.createElement('div');
      formulaEl.style.paddingLeft = (l.depth || 0) * 18 + 'px';
      if (l.depth && document.documentElement.dir === 'rtl') {
        formulaEl.style.paddingLeft = '0';
        formulaEl.style.paddingRight = (l.depth || 0) * 18 + 'px';
      }
      formulaEl.innerHTML = l.formula;
      row.appendChild(formulaEl);

      var ruleEl = document.createElement('div');
      ruleEl.className = 'fitch-rule';
      ruleEl.textContent = l.rule;
      row.appendChild(ruleEl);

      proofDiv.appendChild(row);
    });

    containerEl.appendChild(proofDiv);
  };

  // ---------------------------------------------------------------------------------------------- 4. DPLL Trace Visualizer
  /**
   * Renders a DPLL execution trace
   * @param {HTMLElement} containerEl 
   * @param {Object[]} steps [{ step: 1, action: 'Propagation unitaire', lit: 'p', clauses: '{{q, r}, {¬q}}', result: 'sat|unsat|continue' }]
   */
  LogicTools.renderDPLLTrace = function (containerEl, steps, isFa) {
    if (!containerEl) return;
    var wrap = document.createElement('div');
    wrap.className = 'dpll-tree';

    var title = document.createElement('h4');
    title.style.margin = '0 0 0.8rem 0';
    title.textContent = isFa ? '🌳 ردگیری الگوریتم DPLL' : '🌳 Trace de l\'algorithme DPLL';
    wrap.appendChild(title);

    steps.forEach(function (s) {
      var node = document.createElement('div');
      node.className = 'dpll-node' + (s.result === 'sat' ? ' dpll-sat' : (s.result === 'unsat' ? ' dpll-unsat' : ''));

      var badge = document.createElement('span');
      badge.className = 'dpll-step-badge badge-accent';
      badge.textContent = (isFa ? 'گام ' : 'Étape ') + s.step;
      node.appendChild(badge);

      var act = document.createElement('strong');
      act.textContent = s.action + ' : ';
      node.appendChild(act);

      var detail = document.createElement('span');
      detail.innerHTML = s.detail;
      node.appendChild(detail);

      var clDiv = document.createElement('div');
      clDiv.style.marginTop = '0.4rem';
      clDiv.style.color = 'var(--muted)';
      clDiv.innerHTML = '<strong>' + (isFa ? 'مجموعه بندها Σ = ' : 'Clauses résiduelles Σ = ') + '</strong>' + s.clauses;
      node.appendChild(clDiv);

      wrap.appendChild(node);
    });

    containerEl.appendChild(wrap);
  };

})();

