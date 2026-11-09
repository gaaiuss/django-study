# Django Forms

Django forms can be configured in various ways. See more about in the official
docs - [Django Forms](https://docs.djangoproject.com/en/6.1/topics/forms/#building-a-form-in-django)

## From zero

You can import django forms from `from django import forms` to create your forms
based on a class inheritance:

```python
class RegisterForm(forms.ModelForm)
```

You can edit your Meta class as well to change ou rewrite some attrs from the
parent class:

```python
class Meta:
  model = User
  # Setting fields manually
  fields = ["username", "first_name", "last_name", "email", "password"]

  # exclude = ["first_name"] # Leaving only setted fields here.

  # Rewriting filed label
  labels = {
      "username": "Username:",
      "first_name": "First Name:",
      "last_name": "Last Name:",
      "password": "Password:",
      "email": "E-mail:",
  }

  # These fields can be modified to rewrite some fields. As we are creating
  # then above, we do not need to use then.

  # help_texts = {
  #     "email": "E-mail must be valid.",
  # }

  # error_messages = {
  #     "username": {
  #         "required": "This field is required.",
  #     },
  # }

  # widgets = {
  #     "password": forms.PasswordInput(
  #         attrs={
  #             "placeholder": "Type your password here.",
  #         },
  #     ),
  # }
```

It is for best pratice to rewrite django default fields from the declaration,
like:

```python
password = forms.CharField(
    required=False,
    widget=forms.PasswordInput(attrs={"placeholder": "Your password."}),
)
```

There we have declared and rewrite the password field passing the custom addons
right from the declaration.
