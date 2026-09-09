from django.urls import path

from .views import blog_view, index

urlpatterns = [
    path("", index),
    path("view/", blog_view),
]
