# Templates

Templates can be separated in any way you want. By default they are stored in
`templates` folder inside each app (this includes the project itself).

To create a central template folder or at any other location you want, you can
specify the path on the `settings.py` `TEMPLATES` in the `DIRS` list inside the
project, e.g.: `"DIRS": [ BASE_DIR / "base"]`.

## 1. Extends

Django allows inheritance between templates using the `% extends %` word inside
the html. This allows you to create a base template and extend it after on other
templates inside an app for example.

## 2. Include

You can import a whole html template using the `% include %` command inside any
other template. You need to specify the whole path to the template you want to
include, e.g.: `{% include 'global/partials/head.html' %}`.

## 3. Block

The `{% block %}` tag is a placeholder for information, is meant to be set on a
parent template (like on this project under `base/global/index.html`) to be
replaced on a child template (on this caseon blog and home). This can be used
to set various options of code blocks (almost like a inheritance relation) on a
base template and, later on the other child templates, replace them with the
actual code. _A block DOES NOT WORK inside on a included file_.

## 4. Template URLs

URLs in templates can be referenced with the tag `{% url 'url_name' %}` and as
said before, you can use the `app_name` namespace to specify the url name:
`blog:index`.

## 5. For loop

You can also use a for loop in a template as well using:
`{% for variable in iterable %} "for content" {% endfor %}` 'iterable' being
the view context key/value.

If you use a include inside a for, e.g.:
`{% include 'global/partials/post_block.html' %}` the template `post_block`
can use the post variable created by the for loop using `{post.key}`.

## 6. If

Like the for, you can use if inside a template:
`{% if condition %} "if content" {% else %} "else content" {% endif %}`
And:
`{% if condition %} "if content" {% elif condition %} "else if content" {% endif %}`
