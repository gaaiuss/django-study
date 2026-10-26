Basic commands

# Start a new project

```sh
django-admin startproject <project_name> .
```

`django-admin`: is a command that allows you to do various admin-like actions,
like start a project for example. In the majority of cases, we use django-admin
to start a new project.
`startproject`: command to create a new project
`.`: path to where the project will be installed

# Create an app

```sh
python manage.py startapp <app_name>
```

`manage.py`: file that is created after the startproject command. It substitutes
the django-admin as a base command.
`startapp`: creates a new app.

Remember to add your app on your `settings.py`.

---

# Collect static files

```sh
python manage.py collectstatic
```

`collectstatic`: Collect all static files from apps and add them to the STATIC_ROOT
diretory.

# Create super user

```sh
python manage.py createsuperuser
```

`createsuperuser`: This command creates the ultimate privilege user that allows
many Django operations, including access to the admin area.
`AUTH_PASSWORD_VALIDATORS`: is the project setting that checks the password
strength, you can check it in your `project/settings.py`.

# Change password

```sh
python manage.py createsuperuser
```

For created users only.

# Migrations

```sh
python manage.py makemigrations
```

Create new migration files based on your models changes.

```sh
python manage.py migrate
```

Apply/unapply migrations to your database.
