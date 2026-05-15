const CACHE_NAME = 'hn-digests-7e7f8e88';
const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './favicon.ico',
  './sw.js',
  './2026-05-15.html',
  './2026-05-15.epub',
  './2026-05-15.md',
  './2026-05-15.txt',
  './2026-05-14.html',
  './2026-05-14.epub',
  './2026-05-14.md',
  './2026-05-14.txt',
  './2026-05-13.html',
  './2026-05-13.epub',
  './2026-05-13.md',
  './2026-05-13.txt',
  './2026-05-11.html',
  './2026-05-11.epub',
  './2026-05-11.md',
  './2026-05-11.txt',
  './2026-05-09.html',
  './2026-05-09.epub',
  './2026-05-09.md',
  './2026-05-09.txt',
  './2026-05-08.html',
  './2026-05-08.epub',
  './2026-05-08.md',
  './2026-05-08.txt'
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
