const { defineConfig } = require('@vue/cli-service');
const NodePolyfillPlugin = require("node-polyfill-webpack-plugin");
module.exports = defineConfig({
  transpileDependencies: true,
  configureWebpack: {
    plugins: [new NodePolyfillPlugin()],
    optimization: {
      splitChunks: {
        chunks: "all",
      },
    },
  },
  // devServer: {
  //   proxy: {
  //     '^/': {
  //       // for local development, won't work after building
  //       target: process.env.VUE_APP_DEV_BACKEND_URL,
  //       changeOrigin: true,
  //       ws: false,
  //       pathRewrite: {
  //         '^/': '/'
  //       },
  //     }
  //   }
  // },
})
