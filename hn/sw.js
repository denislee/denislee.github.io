const CACHE_NAME = 'hn-digests-v1';
const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './favicon.ico',
  './2026-04-17.html',
  './2026-04-17.epub',
  './2026-04-16.html',
  './2026-04-16.epub',
  './2026-04-15.html',
  './2026-04-15.epub',
  './2026-04-14.html',
  './2026-04-14.epub',
  './2026-04-13.html',
  './2026-04-13.epub'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});