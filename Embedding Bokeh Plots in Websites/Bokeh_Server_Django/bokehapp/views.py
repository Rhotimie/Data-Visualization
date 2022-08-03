from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from . import BasicLine

# Create your views here.


def index(request):
    context = {
        "div": BasicLine.div,
        "js": BasicLine.js,
        "cdn_js": BasicLine.cdn_js,
        "cdn_css": BasicLine.cdn_css,
    }
    return render(request, "bokehapp/index.html", context)
