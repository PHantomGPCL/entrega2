from django.shortcuts import render,redirect
from django.views.generic import TemplateView
# Create your views here.



class Inicio(TemplateView):
    template_name = 'index.html'
