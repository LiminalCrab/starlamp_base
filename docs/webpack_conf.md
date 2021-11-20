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
in the /templates/base.html file.

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
Useful for when we have hashes in our filename which changes every compilation.

#### babel-loader
https://webpack.js.org/loaders/babel-loader/

#### clean-webpack-plugin
this plugin will remove all files inside webpack's output.path directory, as well as all unused webpack assets after 
every successful rebuild.

dangerouslyAllowCleanPatternsOutsideProject is set to true, this allows cleaning patterns to run in the project directory.








#### entry
Usage: `entry: string | [string]`
Usage (object syntax): `entry: { <entryChunkName> string | [string] } | {}`

An entry point indicates which module webpack should use to begin building 
the internal dependency graph. It figures out the other modules and libs that entry point dependends on
directly and indirectly.

**Examples**

Shorthand
```javascript
module.exports = {
  entry: './path/to/my/entry/file.js',
};
```

Long...hand?
```javascript
module.exports = {
  entry: {
    main: './path/to/my/entry/file.js',
  },
};
```

Passing lists
```javascript
module.exports = {
  entry: ['./src/file_1.js', './src/file_2.js'],
  output: {
    filename: 'bundle.js',
  },
};
```
##### EntryDescription object
An object with an entry point description.

runtime and dependOn should not be used together on a single entry.

`dependOn`: Entry point that the current entry point depends on.

`filename`: specifies the name of each output file on disk.

`import`: module(s) that are loaded upon startup.

`library`: Specify library options to bundle a library from current entry.

`runtime`:  The name of the runtime chunk. When set, a new runtime chunk will be created. It can be set to false to avoid a new runtime chunk since webpack 5.43.0. [????]

`publicPath`: Specify a public URL address for the output files of this entry when they are referenced in a browser. Also see output.publicPath. [omg this will be great for interfacing with other shit]

###### Separate App and Vendor entries.

This is two separate entry points that imports required libs/files which aren't modified (Bootstrap, Jquery, images). 
It bundles them together into their own chunk, and somhow the hash remains the same because magic so browsers cache it faster.
Reducing loadtime.

```javascript
module.exports = {
  entry: {
    main: './src/app.js',
    vendor: './src/vendor.js',
  },
};
```
###### Multipage application
Probably the most important thing here. As a rule of thumb: Use exactly one entry point for each HTML document. 

```javascript
module.exports = {
  entry: {
    pageOne: './src/pageOne/index.js',
    pageTwo: './src/pageTwo/index.js',
    pageThree: './src/pageThree/index.js',
  },
};
```

#### output
Tells webpack where to emit the bundles it creates and how to name these files.
Webpack's default is ./dist/main.js
Starlamp, however, uses: ./galleries/static/galleries/dist/main.js

For more than a single chunk, use multiple entry points.
Otherwise, it's this easy.

```javascript
module.exports = {
  output: {
    filename: 'bundle.js',
  },
};
```

#### loaders
https://webpack.js.org/concepts/loaders/
Webpack only understands JavaScript and JSON files. Loaders allow it to process other types of files,
then converts them into valid modules that can be consumed by the application and added to the dependency graph.

If we deicde to go with SCSS, we'll need this. For now, that's undecided.

##### Properties of a loader
The **test** property identifies which file or files should be transformed.

The **use** property indicates which loader should be used to do the transforming.

```javascript
const path = require('path');

module.exports = {
  output: {
    filename: 'my-first-webpack.bundle.js',
  },
  module: {
    rules: [{ test: /\.txt$/, use: 'raw-loader' }],
  },
};
```
**Warning**: When defining rules in the config, they're being defined under module.rules, not rules. 
Webpack should warn you if you have done this incorrectly.

**Warning**: When regex matching, don't quote anything. It's not the same. IE: /\.txt$/ vs '/\.txt$/' Unquoted regex informs webpack to match
and file that ends with a .txt, and quoted text instructs webpack to match a single file with an absolute path of .txt
##### Plugins
Plugins for loaders can be used to perform a bunch of different tasks like bundle optimization, asset management, and injection of
environment variables. All of this is very yikes and sounds like a supplychain nightmare. 

Oh, that's cool they're the **BACKBONE** of Webpack. _AMAZING_.
https://webpack.js.org/concepts/plugins/

#### Mode
Setting this parameter to "development", "production", or "none" can enable
webpack's built-in optimization that corresponds to each environment. Default value is production.

Change this to development, change it back to production after the fact.

### Modules
https://webpack.js.org/concepts/modules/

# Targets
Deployment targets. Can have multiple targets.
What's a target? I guess it's a target environment... like a node environment 

Oh fuck yeah this part of the docs isn't even finished yet that's why it explains nothing.

