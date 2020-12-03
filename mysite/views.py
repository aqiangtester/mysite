#!/usr/bin/env python30
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def page_not_found(request):
    # return render(request, "404.html")
    html = "<html><body>404</body></html>"
    return HttpResponse(html)

def page_error(request):
    return render(request, "500.html")

def permission_denied(request):
    return render(request, "403.html")

def bad_request(request):
    return render(request, "400.html")