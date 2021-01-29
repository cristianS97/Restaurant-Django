from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.contrib.auth import logout as do_logout
from django.contrib import messages

# Create your views here.
def logout(request):
    do_logout(request)
    return redirect('index')

