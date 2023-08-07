from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class IntroTemplateView(TemplateView):
    model = User
    template_name = 'introapp/main.html'
