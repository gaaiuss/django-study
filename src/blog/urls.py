from django.urls import path

from blog.views import index, post

app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("<int:post_id>/", post, name="post"),
]
