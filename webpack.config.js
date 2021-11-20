const path = require("path");
const {CleanWebpackPlugin} = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
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
            filename: "[name].js",
            chunkFilename: "[id]-[chunkhash].js",
        },
        devServer: {
            port: 8081,
            watchFiles: ['assets/**/*', 'galleries/static/**'],
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
                    test: /\.css$/,
                    exclude: exclusions,
                    use: [
                        MiniCssExtractPlugin.loader,
                        {loader: "css-loader"},
                    ],
                },
            ],
        },
        plugins: [
            new CleanWebpackPlugin({cleanStaleWebpackAssets: false}),
            new MiniCssExtractPlugin(),
        ],
    },
];