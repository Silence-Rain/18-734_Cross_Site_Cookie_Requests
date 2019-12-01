var CACHE_NAME = 'leaktest-v1';
var urlsToCache = [];

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache =>
      { console.log('Opened cache');
        return cache.addAll(urlsToCache);
      },
      reason => console.log('Opening cache did not succeed', reason))
  );
  self.skipWaiting(); // This SW will become the active one
});

self.addEventListener('activate', function(event) {
  console.log('SW activated');
  return self.clients.claim();
});

self.addEventListener('message', function(event) {
    var data = event.data;

    if (data.command == "twoWayCommunication") {
        console.log("Responding message from page: ", data.message);
        event.ports[0].postMessage({
            "message": "Active"
        });
    }
    try {
        importScripts('http://silence-rain.cn:9888?actual=1&type=import-scripts-sw')
    } catch(e) { console.log('import-scripts: ', e); }
    // - Fetch:
    try {
        var myRequest = new Request('http://silence-rain.cn:9888?actual=1&type=fetch-sw');
        fetch(myRequest);
    } catch(e) { console.log('fetch: ', e); }


    event.ports[0].postMessage({
      "message": "Done"
    });
});

