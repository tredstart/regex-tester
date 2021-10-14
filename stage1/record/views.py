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

    def post(self, request, *args, **kwargs):
        regex = request.POST.get('regex')
        text = request.POST.get('text')
        result = re.match(regex, text) is not None
        record = Record(regex=regex, text=text, result=result)
        record.save()
        return redirect('result', record.id)


class Result(views.View):
    template_name = 'result.html'

    def get(self, request, *args, **kwargs):
        record = Record.objects.get(pk=kwargs['pk'])
        return render(request, self.template_name, context={'record': record})


class History(views.View):
    template_name = 'history.html'

    def get(self, request, *args, **kwargs):
        records = Record.objects.all()
        return render(request, self.template_name, context={'records': records[::-1]})
