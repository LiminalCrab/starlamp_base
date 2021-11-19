const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'galleries/static'),
    filename: '[name].js',
    chunkFilename: "[id]-[chunkhash].js",
  },
  devServer: {
    writeToDisk: true,
  }
};