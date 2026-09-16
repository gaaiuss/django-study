### Django Study

Django is a framework to develop websites.

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

#### URLs

The apps URLs point to a view that can be:

- function based:
  1. Add an import: from my_app import views
  2. Add a URL to urlpatterns: path('', views.home, name='home')

- class based:
  1. Add an import: from other_app.views import Home
  2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')

URLs can be nested inside a urls file that you can create on each app and within
each file there is a method to nest all the urls in the main project urls file,
the `include()`, e.g.:

1. Import the include() function: from django.urls import include, path
2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))

To use urls in templates you have to specify a name to it under the path method
`path('', views.blog, name='index')`. Even better is to set a namespace on the
top of the urls.py file to get a better name later when using urls on templates
`app_name = blog` so it will look like `blog:index` on the template.

---

#### Views

Views are the functions or classes that render the templates. They receive a
http request and returns a http response as a normal http communication.

There you can manipulate the request, specifiy the response template redirection
path (the page to respond) and manipulate the context.

The context is a data structure in form of a dictionary which you can send data
to the templates. To use it, you can declare a dictionary especifying the key
value data, and use the key on the template to get the value.

---

#### Templates

Templates can be separated in any way you want. By default they are stored in
`templates` folder inside each app (this includes the project itself).

To create a central template folder or at any other location you want, you can
specify the path on the `settings.py` `TEMPLATES` in the `DIRS` list inside the
project, e.g.: `"DIRS": [ BASE_DIR / "base"]`.

Django allows inheritance between templates using the `% extends %` word inside
the html. This allows you to create a base template and extend it after on other
templates inside an app for example.

You can import a whole html template using the `% include %` command inside any
other template. You need to specify the whole path to the template you want to
include, e.g.: `% include 'global/partials/head.html' %`.

The `% block %` tag is a placeholder for information, is meant to be set on a
parent template (like on this project under `base/global/index.html`) to be
replaced on a child template (on this caseon blog and home). This can be used
to set various options of code blocks (almost like a inheritance relation) on a
base template and, later on the other child templates, replace them with the
actual code. _A block DOES NOT WORK inside on a included file_.

URLs in templates can be referenced with the tag `{% url 'url_name' %}` and as
said before, you can use the `app_name` namespace to specify the url name:
`blog:index`.

---

#### Static files

Static files are all the files you will want to use as essential files needed for
the application to work, like images, css files and script files.

For a first setup you can create the static folder on the project root, but if
you want to, you can create it on another location, you just need to specify
the `STATICFILES_DIRS = []`, in the `settings.py` on your project, the location
of your new static folder.

To use the reference of the static files dir, we use tne tag `{% load static %}`
on the top of the template file we want to use it and the `{% static %}` command
on the the link reference, e.g.:`{% static 'assets/css/styles.css'%}`.

---

### Basic commands

`django-admin`: is a command that allows you to do various admin-like actions,
like start a project for example. In the majority of cases, we use django-admin
to start a new project.

```sh
django-admin startproject <project_name> .
```

- `startproject`: command to create a new project
- `.`: path to where the project will be installed

`manage.py`: file that is created after the startproject command. It substitutes
the django-admin as a base command.

`startapp`: creates a new app.

```sh
python manage.py startapp <app_name>
```

---
