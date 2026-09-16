from typing import TYPE_CHECKING

from django.shortcuts import render

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse

# Create your views here.


def home_view(request: HttpRequest) -> HttpResponse:
    context = {
        "text": "This is the home view context",
    }
    return render(
        request,
        "home/index.html",
        context,
    )
