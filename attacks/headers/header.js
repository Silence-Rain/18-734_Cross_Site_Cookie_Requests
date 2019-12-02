const http = require('http');

http.createServer(function (req, res) {
  res.writeHead(200, {
  	'Content-Security-Policy': 'default-src "none"; report-uri http://silence-rain.cn:9888?ad_type=1&type=header-csp',
  	'X-Content-Security-Policy': 'default-src "none"; report-uri http://silence-rain.cn:9888?ad_type=1&type=header-x-csp',
  	'Content-Security-Policy-Report-Only': 'default-src "none"; report-uri http://silence-rain.cn:9888?ad_type=1&type=header-csp-only',
  	'Link': ' <http://silence-rain.cn:9888?ad_type=1&type=link-stylesheet>; rel="stylesheet"'
  });
  res.end("headers\n");
}).listen(9777);
