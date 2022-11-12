const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '^/': {
        // for local development, won't work after building
        target: 'http://localhost:8000',
        changeOrigin: true,
        ws: false,
        pathRewrite: {
          '^/': '/'
        },
      }
    }
  },
})
