import re

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import views

# Create your views here.
from .models import Record


class Home(views.View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

