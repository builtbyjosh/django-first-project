from django.shortcuts import render
from django.http import (
    HttpResponse,
    Http404,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.urls import reverse


def simple_view(request):
    return render(request, "my_app/example.html")
