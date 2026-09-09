### Django study

Django is a framework to develop websites.

Django follows the Model View Template (MVT):

- _Model_: handles all the data interactions (database).
- _View_: its the intermediate element between the client and the host. It
  receives a HTTP request and decides what to do based on that request. In
  simple terms, the view is a function (could be a class too) that receives
  a HTTP request and must return a HTTP response.
- _Template_:

We do not work directly in the `project/` directory. Django uses apps to separate
the whole application in little pieces to better organize and manage all the
components. The organization and separation of a piece of the application
into apps is totally developer charged, you decide how the apps will look like
and how they will be separated.

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
