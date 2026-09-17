# Create your views here.
from typing import TYPE_CHECKING

from django.http import Http404
from django.shortcuts import render

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


from blog.data import posts


def index(request: HttpRequest) -> HttpResponse:
    template = "blog/index.html"
    context = {
        # "text": "This is the blog index context",
        "title": "Blog - ",
        "posts": posts,
    }
    return render(request, template, context)


def post(request: HttpRequest, post_id: int) -> HttpResponse:
    post_found: dict[str, int | str] | None = None

    for post in posts:
        if post["id"] == post_id:
            post_found = post
            break

    if post_found is None:
        msg = "Post does not exists!"
        raise Http404(msg)

    template = "blog/post.html"
    context = {
        "title": f"{post_found['title']} - ",
        "post": post_found,
    }
    return render(request, template, context)
