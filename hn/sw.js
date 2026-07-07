const CACHE_NAME = 'hn-digests-deaf6d97';
const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './favicon.ico',
  './sw.js',
  './2026-07-07.html',
  './2026-07-07.epub',
  './2026-07-07.md',
  './2026-07-07.txt',
  './2026-07-07.rsvp',
  './2026-07-05.html',
  './2026-07-05.epub',
  './2026-07-05.md',
  './2026-07-05.txt',
  './2026-07-05.rsvp',
  './2026-07-04.html',
  './2026-07-04.epub',
  './2026-07-04.md',
  './2026-07-04.txt',
  './2026-07-04.rsvp',
  './2026-07-03.html',
  './2026-07-03.epub',
  './2026-07-03.md',
  './2026-07-03.txt',
  './2026-07-03.rsvp',
  './2026-07-02.html',
  './2026-07-02.epub',
  './2026-07-02.md',
  './2026-07-02.txt',
  './2026-07-02.rsvp',
  './2026-06-30.html',
  './2026-06-30.epub',
  './2026-06-30.md',
  './2026-06-30.txt',
  './2026-06-30.rsvp'
];

self.addEventListener('install', (event) => {
  self.skipWaiting();
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    // Add each asset individually so one missing/slow file doesn't abort install.
    await Promise.all(ASSETS.map(a => cache.add(a).catch(err => {
      console.warn('sw: precache skipped', a, err);
    })));
  })());
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  event.respondWith((async () => {
    const cached = await caches.match(req, {ignoreSearch: true});
    if (cached) return cached;
    try {
      const resp = await fetch(req);
      if (resp && resp.ok && resp.type === 'basic') {
        const cache = await caches.open(CACHE_NAME);
        cache.put(req, resp.clone());
      }
      return resp;
    } catch (err) {
      // Offline and not cached — fall back to the index for HTML navigations.
      if (req.mode === 'navigate' || req.destination === 'document') {
        const fallback = await caches.match('./index.html');
        if (fallback) return fallback;
      }
      throw err;
    }
  })());
});
