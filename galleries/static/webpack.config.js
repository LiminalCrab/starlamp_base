module.exports = {
    entry: {
        app: './src/index.js'
    },
    mode: 'development',
    watch: true,
    devtool: 'source-map',
    output: {
        filename: 'index.js',
        path: 'starlamp_base/galleries/static/galleries/js',
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
            }
        ]
    },
    resolve: {
        extensions: [
            '.js',
            '.css'
        ]
    }
};