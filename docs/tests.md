# Tests

From now on, we will give a brief introdution about Python tests in general
and after a Django focused test explanation.

## Tests with Python in general

To make things simple we use [Pytest](https://docs.pytest.org/en/stable/)
framework to write small readable automatic tests.

## Configuration - pytest.ini

To configure it we use a `.ini` file to stablish some rules:

```ini
[pytest]

; path where your django project settings.py is
DJANGO_SETTINGS_MODULE = project.settings

; test naming conventions: these are used by pytest to locate all test files
; inside your project.
python_files = test.py tests.py test_*.py tests_*.py *_test.py *_tests.py

; pytest attributes
addopts =
  --doctest-modules
  ; pytest is now able to execute doctests (tests via docstring)
  ; you is now able to classify (mark) a test with custom markers. The strict
  ; word, tells pytest to use olny your custom markers.
  --strict-markers

; put your markers here.
markers =
  slow: Run slow tests
  fast: Run fast tests
```

## Naming convention

As commented above, you can configure pytest to read various types of files
specifying the name inside your `pytest.ini` file.

When we talk about tests in itself there are a convention to start a test function
with "test\_" and to be to most specifc possible with the test name:
`def (test_recipe_home_template_shows_no_recipes_if_no_recipes_were_found)`

## Test in Django

Django uses the TestCase class to store and run its test, so to create your tests
classes, remember to inherit from `from django.test import TestCase`.
