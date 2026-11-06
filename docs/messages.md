# Messages

Django messages docs:
[Django Messages](https://docs.djangoproject.com/en/6.1/ref/contrib/messages/)

Django use a system of flash messages: messages that are loaded once, and if
the problem is solved in case of an error for example, the message will clear.
Messages will be cleared once the user see them.

You can edit your messages css by using the constant var MESSAGE_TAGS in your
django project `settings.py`:

```python
MESSAGE_TAGS = {
    constants.DEBUG: "message-debug",
    constants.ERROR: "message-error",
    constants.INFO: "message-info",
    constants.SUCCESS: "message-success",
    constants.WARNING: "message-warning",
}
```

Import messages:

```python
from django.contrib import messages
```

Message example:

```python
messages.success(request, "Home view loaded successful.")
```
