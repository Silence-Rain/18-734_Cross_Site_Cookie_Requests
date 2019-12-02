const http = require('http');

http.createServer(function (req, res) {
  res.writeHead(302, {
    'Location': 'http://silence-rain.cn:9888?ad_type=1&type=redirect-302'
  });
  res.end("302 redirecting\n");
}).listen(9777);