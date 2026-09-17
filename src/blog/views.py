# Create your views here.
from typing import TYPE_CHECKING

from django.shortcuts import render

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


from blog.data import posts


def index(request: HttpRequest) -> HttpResponse:
    context = {
        # "text": "This is the blog index context",
        "title": "Blog - ",
        "posts": posts,
    }
    return render(request, "blog/index.html", context)
