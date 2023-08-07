from django.urls import path

from introapp.views import landing

app_name = "introapp"

urlpatterns = [

    path('', landing, name='main'),

]