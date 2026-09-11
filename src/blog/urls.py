from django.urls import path

from .views import blog_view, index

app_name = "blog"

urlpatterns = [
    path("", index, name="home"),
    path("view/", blog_view, name="view"),
]
