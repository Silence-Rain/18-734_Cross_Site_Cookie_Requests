const http = require('http');

http.createServer(function (req, res) {
  res.writeHead(200, {
    'Set-Cookie': 'leak_test=1;Expires=Wed, 13-Jan-2020 22:23:01 GMT'
  });
  res.end("cookie has been set\n");
}).listen(9888);