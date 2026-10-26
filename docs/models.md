# Models

Models are the source of your database, generaly referes to a single database.
A model is another class that inherits the `models.Model` class, and each
attribute is a database field. The primary key field is created automatically.

`__str__` method on a model is used iside various parts inside Django, but mainly
on the admin area, like the name of a instance of the model is shown on the django
models object list.

## 1. Attributes/Fields

Like any other SQL database, Django models follow the same structure but with
different names.

For more details access the docs:
[Model Fields](https://docs.djangoproject.com/en/6.1/ref/models/fields/)
