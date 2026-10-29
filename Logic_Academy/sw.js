/* Logic Academy - Service Worker for 100% Offline Studying */
const CACHE_NAME = 'logic-academy-v1';

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll([
        './',
        './index.html',
        './manifest.json',
        './css/base.css',
        './css/book.css',
        './css/pages.css',
        './css/interactive.css',
        './assets/vendor/fonts.css',
        './assets/vendor/katex/katex.css',
        './js/core.js',
        './js/store.js',
        './js/common.js',
        './js/logic-tools.js',
        './js/view-home.js',
        './js/view-lesson.js',
        './js/view-annales.js',
        './js/view-glossary.js',
        './js/view-me.js',
        './js/app.js',
        './data/build.js',
        './data/ui.js',
        './data/index.js',
        './data/glossary.js',
        './data/annales.js'
      ]).catch((err) => {
        console.warn('Cache install partial:', err);
      });
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key))
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    }).catch(() => {
      return caches.match('./index.html');
    })
  );
});

