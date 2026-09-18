# Django Study

Django is a framework to develop websites. _It is not a server!_

## Details

Django follows the Model View Template (MVT):

- _Model_: handles all the data interactions (database).
- _View_: its the intermediate element between the client and the host. It
  receives a HTTP request and decides what to do based on that request. In
  simple terms, the view is a function (could be a class too) that receives
  a HTTP request and must return a HTTP response.
- _Template_: where you store and renderize all your html files.

We do not work directly in the `project/` directory. Django uses apps to separate
the whole application in little pieces to better organize and manage all the
components. The organization and separation of a piece of the application
into apps is totally developer charged, you decide how the apps will look like
and how they will be separated.

---

### URLs

The apps URLs point to a view that can be:

- function based:
  1. Add an import: from my_app import views
  2. Add a URL to urlpatterns: path('', views.home, name='home')

- class based:
  1. Add an import: from other_app.views import Home
  2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')

URLs can be nested inside a urls file created on each app. On the project urls
there is a method to nest all the urls in the main project urls file,
the `include()`, e.g.:

1. Import the include() function: from django.urls import include, path
2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))

#### URLs inside templates

To use urls in templates you have to specify a name to it under the path method
`path('', views.blog, name='index')`. Even better is to set a namespace on the
top of the urls.py file to get a better name later when using urls on templates
`app_name = blog` so it will look like `blog:index` on the template.

#### Dinamic URLs

Dinamic URLs can be used informing a variable after the path, like:
`path("post/<int:post_id>/", post, name="post")` where the `<post_id>` can be
any variable that you want to become dinamic and the `int:` is the type of it.

After defining it on the urls, you must also receive the variable on the view
related to it. The name must be the same:
`def post(request: HttpRequest, post_id: int) -> HttpResponse:`

To use it inside the template you use this signature:
`{% url 'blog:post' post.id %}` where `'blog:post'` is the url from the app and
`post.id` is the parameter defined on the app view.

Always specify the type of the variable, they can be:

- `int`: Matches zero or any positive integer. Returns an int.
- `str`: Matches any non-empty string, excluding the path separator, '/'.
  This is the default if a converter isn’t included in the expression.
- `slug`: Matches any slug string consisting of ASCII letters or numbers, plus
  the hyphen and underscore characters. For example, `your-1st-django-site`.
- `uuid`: Matches a formatted UUID. To prevent multiple URLs from mapping to
  the same page, dashes must be included and letters must be lowercase. For
  example, 075194d3-6885-417e-a8a8-6c931e272f00. Returns a UUID instance.
- `path`: Matches any non-empty string, including the path separator, '/'.
  This allows you to match against a complete URL path rather than a segment of
  a URL path as with str.

---

### Views

Views are the functions or classes that render the templates. They receive a
http request and returns a http response as a normal http communication.

There you can manipulate the request, specifiy the response template redirection
path (the page to respond) and manipulate the context.

#### Context

The context is a data structure in form of a dictionary which you can send data
to the templates. To use it, you can declare a dictionary especifying the key
value data, and use the key on the template to get the value.

---

### Templates

Templates can be separated in any way you want. By default they are stored in
`templates` folder inside each app (this includes the project itself).

To create a central template folder or at any other location you want, you can
specify the path on the `settings.py` `TEMPLATES` in the `DIRS` list inside the
project, e.g.: `"DIRS": [ BASE_DIR / "base"]`.

#### Extends

Django allows inheritance between templates using the `% extends %` word inside
the html. This allows you to create a base template and extend it after on other
templates inside an app for example.

#### Include

You can import a whole html template using the `% include %` command inside any
other template. You need to specify the whole path to the template you want to
include, e.g.: `{% include 'global/partials/head.html' %}`.

#### Block

The `{% block %}` tag is a placeholder for information, is meant to be set on a
parent template (like on this project under `base/global/index.html`) to be
replaced on a child template (on this caseon blog and home). This can be used
to set various options of code blocks (almost like a inheritance relation) on a
base template and, later on the other child templates, replace them with the
actual code. _A block DOES NOT WORK inside on a included file_.

#### Template URLs

URLs in templates can be referenced with the tag `{% url 'url_name' %}` and as
said before, you can use the `app_name` namespace to specify the url name:
`blog:index`.

#### For loop

You can also use a for loop in a template as well using:
`{% for variable in iterable %} "for content" {% endfor %}` 'iterable' being
the view context key/value.

If you use a include inside a for, e.g.:
`{% include 'global/partials/post_block.html' %}` the template `post_block`
can use the post variable created by the for loop using `{post.key}`.

#### If

Like the for, you can use if inside a template:
`{% if condition %} "if content" {% else %} "else content" {% endif %}`
And:
`{% if condition %} "if content" {% elif condition %} "else if content" {% endif %}`

---

### Static files

Static files are all the files you will want to use as essential files needed for
the application to work, like images, css files and script files.

For a first setup you can create the static folder on the project root, but if
you want to, you can create it on another location, you just need to specify
the `STATICFILES_DIRS = []`, in the `settings.py` on your project, the location
of your new static folder.

To use the reference of the static files dir, we use tne tag `{% load static %}`
on the top of the template file we want to use it and the `{% static %}` command
on the the link reference, e.g.:`{% static 'assets/css/styles.css'%}`.

#### Static files in production

Django is not a server, static files are not loaded when using django in production
(when debug is `DEBUG = False`), static files inside apps or project are just
used in development.

When you are in production (`DEBUG = True`), you have to configure the allowed
hosts varible inside the settings `ALLOWED_HOSTS = []` and a static files dir
to store all the static files used in devepment to be reflected in production
as well (e.g.: `STATIC_ROOT = BASE_DIR / 'static_files'`).

After all is configured, you can collect all the static files (add to STATIC_ROOT)
with the command: `python manage.py collectstatic`.

---

### Migrations

Migrations are Django's way of propagating model changes into the database.
So everytime you want to apply changes you make to your database, you have to
propagate these migrations to your database.

To apply the changes made on our models we use the `migrate` command to commit
these changes. When you create new migrations (new models), we use the
`makemigrations` command to create new migration files and then apply them with
`migrate` again.

## Basic commands

### Start a new project

```sh
django-admin startproject <project_name> .
```

`django-admin`: is a command that allows you to do various admin-like actions,
like start a project for example. In the majority of cases, we use django-admin
to start a new project.
`startproject`: command to create a new project
`.`: path to where the project will be installed

---

### Create an app

```sh
python manage.py startapp <app_name>
```

`manage.py`: file that is created after the startproject command. It substitutes
the django-admin as a base command.
`startapp`: creates a new app.

---

### Collect static files

```sh
python manage.py collectstatic
```

`collectstatic`: Collect all static files from apps and add them to the STATIC_ROOT
diretory.

---

### Create super user

```sh
python manage.py createsuperuser
```

`createsuperuser`: This command creates the ultimate privilege user that allows
many Django operations, including access to the admin area.
`AUTH_PASSWORD_VALIDATORS`: is the project setting that checks the password
strength, you can check it in your `project/settings.py`.

---

#### Change password

```sh
python manage.py createsuperuser
```

For created users only.

---

### Migrations

```sh
python manage.py makemigrations
```

Create new migration files based on your models changes.

```sh
python manage.py migrate
```

Apply/unapply migrations to your database.
