const http = require('http');
const fs = require('fs');
const path = require('path');

const root = process.cwd();
const port = 8000;
const host = '127.0.0.1';

const types = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
  '.webp': 'image/webp',
  '.ico': 'image/x-icon',
};

http.createServer((req, res) => {
  let url = decodeURIComponent((req.url || '/').split('?')[0]);
  if (url === '/') url = '/index.html';

  const filePath = path.join(root, url);

  fs.stat(filePath, (statErr, stat) => {
    if (statErr || !stat.isFile()) {
      res.statusCode = 404;
      res.end('Not found');
      return;
    }

    fs.readFile(filePath, (readErr, data) => {
      if (readErr) {
        res.statusCode = 500;
        res.end('Error');
        return;
      }

      res.setHeader('Content-Type', types[path.extname(filePath).toLowerCase()] || 'application/octet-stream');
      res.end(data);
    });
  });
}).listen(port, host, () => {
  console.log(`http://${host}:${port}/`);
});
