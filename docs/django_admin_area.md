# Django Admin Area

It is the main interface to manipulate your models in a simple way, do not try
to create your entire front end on it.

## 1. Models

To see/use your model in the Django admin area, you have to register it in the
`admin.py` inside the app where you created your model. As a good pratice/consent
between devs, we create the admin class with: `ModelnameAdmin(admin.ModelAdmin)`
inheriting the admin.ModelAdmin from `django.contrib`. After that, we can use
the `admin.register(YourModel)` decorator passing your model class as a argument
to register the class.

## 2. Attributes/Fields

There is a huge list to look for, see more details in:
[Admin Model Options](https://docs.djangoproject.com/en/6.1/ref/contrib/admin/#modeladmin-options)
