# URLs

The apps URLs point to a view that can be:

- function based:
  1. Add an import: from my_app import views
  2. Add a URL to urlpatterns: path('', views.home, name='home')

- class based:
  1. Add an import: from other_app.views import Home
  2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')

URLs can be nested inside a urls file created on each app. On the project urls
there is a method to nest all the urls in the main project urls file,
the `include()`, e.g.:

1. Import the include() function: from django.urls import include, path
2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))

Aways position your most specific URLs above others in the `url_patterns`.
Django tend to match the first url that he can find in the list, so follow the
rule: _more specific above, more variable bellow_.

## 1. URLs inside templates

To use urls in templates you have to specify a name to it under the path method
`path('', views.blog, name='index')`. Even better is to set a namespace on the
top of the urls.py file to get a better name later when using urls on templates
`app_name = blog` so it will look like `blog:index` on the template.

## 2. Dinamic URLs

Dinamic URLs can be used informing a variable after the path, like:
`path("post/<int:post_id>/", post, name="post")` where the `<post_id>` can be
any variable that you want to become dinamic and the `int:` is the type of it.

After defining it on the urls, you must also receive the variable on the view
related to it. The name must be the same:
`def post(request: HttpRequest, post_id: int) -> HttpResponse:`

To use it inside the template you use this signature:
`{% url 'blog:post' post.id %}` where `'blog:post'` is the url from the app and
`post.id` is the parameter defined on the app view.

Always specify the type of the variable, they can be:

- `int`: Matches zero or any positive integer. Returns an int.
- `str`: Matches any non-empty string, excluding the path separator, '/'.
  This is the default if a converter isn’t included in the expression.
- `slug`: Matches any slug string consisting of ASCII letters or numbers, plus
  the hyphen and underscore characters. For example, `your-1st-django-site`.
- `uuid`: Matches a formatted UUID. To prevent multiple URLs from mapping to
  the same page, dashes must be included and letters must be lowercase. For
  example, 075194d3-6885-417e-a8a8-6c931e272f00. Returns a UUID instance.
- `path`: Matches any non-empty string, including the path separator, '/'.
  This allows you to match against a complete URL path rather than a segment of
  a URL path as with str.

## 3. Utility functions

Some functions that can be very useful when dealing with Django URLs.

### reverse()

Basically return an absolute path given the proper view name:

reverse(_viewname, urlconf=None, args=None, kwargs=None, current_app=None, \*, query=None, fragment=None_)

### resolve()

Returns the view function correspondent to the path given:

resolve(_path, urlconf=None_)

You can use the reverse function as a path given that it returns a path itself:

resolve(_reverse('view:name')_)
