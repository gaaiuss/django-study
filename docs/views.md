# Views

Views are the functions or classes that render the templates. They receive a
http request and returns a http response as a normal http communication.

There you can manipulate the request, specifiy the response template redirection
path (the page to respond) and manipulate the context.

## 1. Context

The context is a data structure in form of a dictionary which you can send data
to the templates. To use it, you can declare a dictionary especifying the key
value data, and use the key on the template to get the value.

## 2. View module

You can create a python package to store all your views, Django understands it
as a single view file. You just need to create a folder named `views` and a
`__init__.py` inside it. After that you can create as many modules as you want,
just remember to import all of them inside your `__init__.py`.

## 3. Query sets

Django has many types of query sets to get data from your database and use it
in your views. For more details see:
[Django Query Sets](https://docs.djangoproject.com/en/6.1/ref/models/querysets/)

For information about filters:
[Django Field Lookups](https://docs.djangoproject.com/en/6.1/topics/db/queries/#field-lookups)
