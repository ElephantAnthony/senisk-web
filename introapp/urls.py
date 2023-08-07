from django.urls import path

from introapp.views import IntroTemplateView

app_name = "introapp"

urlpatterns = [

    path('', IntroTemplateView.as_view(), name='main'),

]