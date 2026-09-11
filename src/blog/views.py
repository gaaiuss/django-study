# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def blog_view(request: HttpRequest) -> HttpResponse:
    print(request)
    return HttpResponse("This is the blog view.")


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Blog - ",
    }
    return render(request, "blog/index.html", context)
