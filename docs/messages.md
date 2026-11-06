# Messages

Django use a system of flash messages: messages that are loaded once, and if
the problem is solved in case of an error for example, the message will clear.
Messages will be cleared once the user see them.

Django messages docs:
[Django Messages](https://docs.djangoproject.com/en/6.1/ref/contrib/messages/)

Import messages:

```python
from django.contrib import messages
```

Message example:

```python
messages.success(request, "Home view loaded successful.")
```
