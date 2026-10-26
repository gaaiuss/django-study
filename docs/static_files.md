# Static files

Static files are all the files you will want to use as essential files needed for
the application to work, like images, css files and script files.

For a first setup you can create the static folder on the project root, but if
you want to, you can create it on another location, you just need to specify
the `STATICFILES_DIRS = []`, in the `settings.py` on your project, the location
of your new static folder.

To use the reference of the static files dir, we use tne tag `{% load static %}`
on the top of the template file we want to use it and the `{% static %}` command
on the the link reference, e.g.:`{% static 'assets/css/styles.css'%}`.

## 1. Static files in production

Django is not a server, static files are not loaded when using django in production
(when debug is `DEBUG = False`), static files inside apps or project are just
used in development.

When you are in production (`DEBUG = True`), you have to configure the allowed
hosts varible inside the settings `ALLOWED_HOSTS = []` and a static files dir
to store all the static files used in devepment to be reflected in production
as well (e.g.: `STATIC_ROOT = BASE_DIR / 'static_files'`).

After all is configured, you can collect all the static files (add to STATIC_ROOT)
with the command: `python manage.py collectstatic`.

## 2. Access static and media files through url in development

In a dev cenario we can use the django urls.py file to configure the static
and media urls the be served by the django itself using:

`urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`
`urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)`

After that, you can access an image for example, through url in django admin or
any part of the project.
