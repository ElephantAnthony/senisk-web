from django.urls import path

from kioskapp.views import SelectSaveUIView, SelectInforView

app_name = "kioskapp"

urlpatterns = [
    path('select_ui/', SelectSaveUIView.as_view(), name='select_ui'),
    path('select_ui/<int:ui>/', SelectSaveUIView.as_view(), name='save_ui'),
    path('information/', SelectInforView.as_view(), name='information'),
    # path('color/', KioskMakeView.as_view(), name='color'),
    # path('menu/', KioskMakeView.as_view(), name='menu'),
    # path('done/', KioskMakeView.as_view(), name='done'),
]