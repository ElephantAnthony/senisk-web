from django.urls import path

from kioskapp.views import ChooseUiView

app_name = "kioskapp"

urlpatterns = [
    path('ui/', ChooseUiView.as_view(), name='ui'),
    # path('information/', KioskMakeView.as_view(), name='information'),
    # path('color/', KioskMakeView.as_view(), name='color'),
    # path('menu/', KioskMakeView.as_view(), name='menu'),
    # path('done/', KioskMakeView.as_view(), name='done'),
]