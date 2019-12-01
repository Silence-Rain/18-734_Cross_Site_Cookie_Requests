const http = require('http');

http.createServer(function (req, res) {
  res.writeHead(200, {
  	"Content-Security-Policy": "default-src 'none'; report-uri http://silence-rain.cn:9888?actual=1&type=csp-report-uri", 
    'Link': ' <http://silence-rain.cn:9888?actual=1&type=link-stylesheet>; rel="stylesheet"'
  });
  res.end("headers\n");
}).listen(9777);