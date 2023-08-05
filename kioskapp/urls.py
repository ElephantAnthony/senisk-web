from django.urls import path

from kioskapp.views import KioskUi, KioskStore, KioskColor, KioskMenu, KioskDone

app_name = "kioskapp"

urlpatterns = [
    path('create/', KioskUi.as_view(), name='ui'),
    path('information/', KioskStore.as_view(), name='information'),
    path('color/', KioskColor.as_view(), name='color'),
    path('menu/', KioskMenu.as_view(), name='menu'),
    path('done/', KioskDone.as_view(), name='done'),
]