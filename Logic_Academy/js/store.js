/* Logic Academy - store: local persistence (read, questions, bookmarks, notes, theme, lang, backup). */
(function () {
  'use strict';
  var Logic = window.Logic;
  var KEY = 'logic_academy_state_v1';
  var memory = null;

  function loadRaw() {
    if (memory) return memory;
    try {
      var s = localStorage.getItem(KEY);
      if (s) return (memory = JSON.parse(s));
    } catch (e) {}
    return (memory = {
      version: 1,
      lang: 'fr',
      theme: 'light',
      read: {},        // { lessonId: timestamp }
      tasks: {},       // { 'lessonId#qId': 1 }
      bookmarks: {},   // { lessonId: timestamp }
      notes: {},       // { lessonId: '...' }
      annalesDone: {}  // { 'exam#ex': 1 }
    });
  }

  function saveRaw() {
    try {
      localStorage.setItem(KEY, JSON.stringify(memory));
    } catch (e) {}
    Logic.bus && Logic.bus.emit && Logic.bus.emit('store:change');
  }

  Logic.store = {
    get: function () { return loadRaw(); },

    getLang: function () { return loadRaw().lang || 'fr'; },
    setLang: function (l) {
      if (Logic.LANGS.indexOf(l) < 0) return;
      loadRaw().lang = l;
      saveRaw();
    },

    getTheme: function () { return loadRaw().theme || 'light'; },
    setTheme: function (th) {
      loadRaw().theme = th === 'dark' ? 'dark' : 'light';
      saveRaw();
    },

    isRead: function (id) { return !!loadRaw().read[id]; },
    setRead: function (id, val) {
      var st = loadRaw();
      if (val) st.read[id] = Date.now();
      else delete st.read[id];
      saveRaw();
    },

    isTaskDone: function (taskId) { return !!loadRaw().tasks[taskId]; },
    setTaskDone: function (taskId, val) {
      var st = loadRaw();
      if (val) st.tasks[taskId] = 1;
      else delete st.tasks[taskId];
      saveRaw();
    },

    isBookmarked: function (id) { return !!loadRaw().bookmarks[id]; },
    toggleBookmark: function (id) {
      var st = loadRaw();
      if (st.bookmarks[id]) delete st.bookmarks[id];
      else st.bookmarks[id] = Date.now();
      saveRaw();
      return !!st.bookmarks[id];
    },

    getNote: function (id) { return loadRaw().notes[id] || ''; },
    setNote: function (id, text) {
      var st = loadRaw();
      if (text && text.trim()) st.notes[id] = text;
      else delete st.notes[id];
      saveRaw();
    },

    isAnnaleDone: function (annaleKey) { return !!loadRaw().annalesDone[annaleKey]; },
    setAnnaleDone: function (annaleKey, val) {
      var st = loadRaw();
      if (val) st.annalesDone[annaleKey] = 1;
      else delete st.annalesDone[annaleKey];
      saveRaw();
    },

    // Progress statistics
    getProgressStats: function () {
      var st = loadRaw();
      var readCount = Object.keys(st.read).length;
      var tasksCount = Object.keys(st.tasks).length;
      var annalesCount = Object.keys(st.annalesDone).length;
      var notesCount = Object.keys(st.notes).length;
      return {
        readCount: readCount,
        tasksCount: tasksCount,
        annalesCount: annalesCount,
        notesCount: notesCount
      };
    },

    exportJSON: function () {
      return JSON.stringify(loadRaw(), null, 2);
    },

    importJSON: function (jsonStr) {
      try {
        var data = JSON.parse(jsonStr);
        if (data && data.version) {
          memory = data;
          saveRaw();
          return true;
        }
      } catch (e) {}
      return false;
    },

    reset: function () {
      memory = {
        version: 1,
        lang: 'fr',
        theme: 'light',
        read: {},
        tasks: {},
        bookmarks: {},
        notes: {},
        annalesDone: {}
      };
      saveRaw();
    }
  };

  // Simple event bus
  var busListeners = {};
  Logic.bus = {
    on: function (evt, fn) {
      (busListeners[evt] = busListeners[evt] || []).push(fn);
    },
    emit: function (evt, arg) {
      var list = busListeners[evt];
      if (list) list.forEach(function (fn) { fn(arg); });
    }
  };
})();

