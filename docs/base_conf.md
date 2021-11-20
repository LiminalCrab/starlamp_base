# API

## Stucture
Nginx <--> Guinicorn <--> Django <--> Postgresql
Nginx <---> Django <--- Webpack


Starlamp (the app) communicates to Nginx (the web server) through guinicorn (Webserver Gateway Interface [WSGI])

When Nginx receives an HTTP request for things like Javascript files, images, ect,
they are handled through a static port and is done soley through Nginx.

Things like python code interpretation get passed to our WSGI via a dynamic port
where it then processes the requested materials, forwards it back to Nginx, and presents
it to the client. 

Requests for stuff that requires python code interpretation gets passed via a dynamic port to our WSGI. The WSGI 
processes the requested material and forwards it back to Nginx. Nginx then presents it to the client.

Webpack SASS workflow
sass-loader compile scss to css
postcss-loader would parse css and add vendor prefixes to CSS rules.
css-loader interprets @import and url() in css.
MiniCssExtractPlugin.loader extract css code to app.css


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

# STATICFILES_STORAGE
ManifestStaticFilesStorage applies an MD5 hash to files stored in the backend. 
The purpose of this is to keep serving old files in case some pages still refer. IE Being cached by the browser or some third party app.

Speeds up load time for subsequent page visits.

Storage backend automatically replaces the paths found in the saved files matching other saved files with the 
path of the cached copy.

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'




# superuser
If a superuser is needed run the command
python manage.py createsuperuser fill in the request information

You can now login to the admin panel.

# static files 
In settings.py starlamp's default directory is set to the project root. This can be changed, or even appended.

# Webpack Configuration
Webpack is a static module bundler, it internally builds a 
dependency graph from one or more entry points and then combines 
every module the project needs into one or more bundles, which are static
assets to serve content from.


### gallery (app)
Handles the images output to the website

### accounts (app)
Handles user accounts, you can create as many of these as you want.

### article (app)
Handles the text in the about me and contact page
