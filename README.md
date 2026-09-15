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

URLs can be nested inside a urls file, within each file there is a method to
nest all the urls in the main project urls file, the `include()`.

---

#### Templates

Templates can be separated in any way you want. By default they are stored in
`templates` folder inside each app (this includes the project itself).

To create a central template folder or at any other location you want, you can
specify the path on the `settings.py` `TEMPLATES` in the `DIRS` list inside the
project, i.e.: `"DIRS": [ BASE_DIR / "base"]`.

Django allows inheritance between templates using the `% extends %` word inside
the html. This allows you to create a base template and extend it after on other
templates inside an app for example.

You can import a whole html template using the `% include %` command inside any
other template. You need to specify the whole path to the template you want to
include, i.e.: `% include 'global/partials/head.html' %`.

You can create a `% block %` to reuse some part of the code, a block of code,
in some other template. Just name it and use the same name to rewrite the same
block on another template.

---

#### Static files

Static files are all the files you will want to use as essential files needed for
the application to work, like images, css files and script files.

For a first setup you can create the static folder on the project root, but if
you want to, you can create it on another location, you just need to specify
the `STATIC_FILES_DIRS`, in the `settings.py` on your project, the location of
your new static folder.

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
