from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:login')
    # 작업을 성공적으로 마치면 연결되는 url
    template_name = 'accountapp/signup.html'
    # 이 화면을 본다..