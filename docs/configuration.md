# API

## Stucture
Nginx --> Guinicorn --> Django --> Postgresql

Starlamp (the app) communicates to Nginx (the web server) through guinicorn (Webserver Gateway Interface [WSGI])

When Nginx receives an HTTP request for things like Javascript files, images, ect,
they are handled through a static port and is done soley through Nginx.

Things like python code interpretation get passed to our WSGI via a dynamic port
where it then processes the requested materials, forwards it back to Nginx, and presents
it to the client. 

Requests for stuff that requires python code interpretation gets passed via a dynamic port to our WSGI. The WSGI 
processes the requested material and forwards it back to Nginx. Nginx then presents it to the client.


# Database Connection
in starlamp_base/settings.py

Modify the database connection, it can be anything from MySQL, MariaDB, to Postgres. So long as you migrate the changes.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'sladmin',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
TIME_ZONE = 'EST'

# superuser
If a superuser is needed run the command
python manage.py createsuperuser fill in the request information

You can now login to the admin panel.

# static files 
In settings.py starlamp's default directory is set to the project root. This can be changed, or even appended.

## Webpack Or: How Extracting The V8 Engine from Chromium Destroyed The Modern Web

Webpack is a static module bundler, it internally builds a 
dependency graph from one or more entry points and then combines 
every module the project needs into one or more bundles, which are static
assets to serve content from.

### Webpack.config.js

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







#### output
Tells webpack where to emit the bundles it creates and how to name these files.
Webpack's default is ./dist/main.js
Starlamp, however, uses: ./galleries/static/galleries/dist/main.js

#### loaders
Webpack only understands JavaScript and JSON files. Loaders allow it to process other types of files,
then converts them into valid modules that can be consumed by the application and added to the dependency graph.

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

#### Mode
Setting this parameter to "development", "production", or "none" can enable
webpack's built-in optimization that corresponds to each environment. Default value is production.

Change this to development, change it back to production after the fact.




### gallery (app)
Handles the images output to the website

### accounts (app)
Handles user accounts, you can create as many of these as you want.

### article (app)
Handles the text in the about me and contact page
