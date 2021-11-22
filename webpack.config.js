const path = require("path");
const {CleanWebpackPlugin} = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const HTMLWebpackPlugin = require('html-webpack-plugin');

const exclusions = /node_modules/;

module.exports = [
    {
        mode: "development",
        entry: {
            app: "./assets/app.js",
        },
        output: {
            path: path.resolve(__dirname, "galleries/static"),
            publicPath: "/static/",
            filename: "js/[name].js",
            chunkFilename: "[id]-[chunkhash].js",
        },
        devServer: {
            port: 8081,
            watchFiles: ['assets/**/*', 'galleries/**/**'],
            devMiddleware: {
                writeToDisk: true,
            }
        },
        module: {
            rules: [
                {
                    test: /.*/,
                    include: path.resolve(__dirname, "assets/image"),
                    exclude: exclusions,
                    options: {
                        context: path.resolve(__dirname, "assets/"),
                        name: "[path][name].[ext]",
                    },
                    loader: "file-loader",
                },
                {
                    test: /\.s?css$/i,
                    exclude: exclusions,
                    use: [MiniCssExtractPlugin.loader, 'css-loader?sourceMap=true', 'postcss-loader', 'sass-loader'],
                },
                {
                    test: /\.js$/,
                    include: path.resolve(__dirname, '/assets'),
                    loader: "babel-loader"
                },
                {
                    test: /three\/examples\/js/,
                    use: 'imports-loader?THREE=three'
                }
            ],
        },
        plugins: [
            new CleanWebpackPlugin({dangerouslyAllowCleanPatternsOutsideProject: true, dry: false}),
            new MiniCssExtractPlugin(),
            new HTMLWebpackPlugin({
                template: path.resolve(__dirname, './assets/index.ejs'),
                filename: path.resolve(__dirname, './galleries/templates/galleries/base.html'),
                inject: false,
            }),
        ],
    },
];