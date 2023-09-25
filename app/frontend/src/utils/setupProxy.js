const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target: 'http://localhost:8080',
      changeOrigin: true,
    })
  );

  app.use(
    '/genshinvoiceapi',
    createProxyMiddleware({
      target: 'https://genshinvoice.top/api?',
      changeOrigin: true,
    })
  );
};
