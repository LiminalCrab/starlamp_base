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


### Starlamp_base

### gallery (app)
Handles the images output to the website

### accounts (app)
Handles user accounts, you can create as many of these as you want.

### article (app)
Handles the text in the about me and contact page