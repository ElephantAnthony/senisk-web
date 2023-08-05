from django.forms import ModelForm

from kioskapp.models import Kiosk


class KioskCreationForm(ModelForm):
    class Meta:
        model = Kiosk
        fields = ['ui', 'type', 'name', 'mainColor', 'subColor']