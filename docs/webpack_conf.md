# Webpack Or: How Repurposing the V8 Engine to Execute JavaScript Outside the Browser Destroyed The Web.
This will be summarized in the future, just getting an idea of what I might need.

Webpack is a static module bundler, it internally builds a 
dependency graph from one or more entry points and then combines 
every module the project needs into one or more bundles, which are static
assets to serve content from.

# What's happening

Webpack is bundling our assets from the 'assets' folder, to the 'galleries/static' folder.
Django is hashing our dev files for us during this process.

'assets/index.html' outputs to 'galleries/static/index.html'

HtmlWebpackPlugin will generate a sl_base.html file which injects the css and js script/links compiled
created by webpack.

sl_base.html -> base.html and subsequent layout chaining.

### the index.ejs file
Don't let this confuse you, this is how we template our html for webpack to inject our scripts.

This .ejs file will contain the Django templating language code to define blocks, and a javascript specific 
templating language, ejs, to inject our scripts into the html. This is necessary because our files are hashed for
easier caching by Django.

Where Django (i guess it's Jinja2 templating language wtv) uses {% %} for templating, Ejs uses <%= %> which is pretty cringe.

So inside the webpack configuration file, we have a path to the /assets/index.ejs file, which points to a file located 
in the /templates/base.html file. At the end of the day, all templates will inherit from the base.html file. **Base.html**
**need to be modified from the index.ejs file. All templates that chain to templates/base.html are safe to be edited from**
**the templates folder.**

Inject is set to false so that HtmlWebpackPlugin does not inject the code automatically.


## Configuration

The entry for the application is
`app: "./assets/app.js`

In dev mode,
`mode: "development`
in production
`mode: "production"`

### Plugins

#### MiniCssExtractPlugin
new MiniCssExtractPlugin({filename: 'css/app.css',}) in the plugins tell Webpack to put all css code into one single file app.css

#### html-webpack-plugin 
Simplifies creation of HTML files to serve webpack bundles.
Useful for when we have hashes in our filename which changes everytime the file compiles.

#### babel-loader
https://webpack.js.org/loaders/babel-loader/

#### clean-webpack-plugin
this plugin will remove all files inside webpack's output.path directory, as well as all unused webpack assets after 
every successful rebuild.

`dangerouslyAllowCleanPatternsOutsideProject` is set to true, this allows cleaning patterns to run in the project directory.
