from django.urls import path

from mainpage.views import landing

app_name = "mainpage"

urlpatterns = [

    path('', landing, name='main'),

]