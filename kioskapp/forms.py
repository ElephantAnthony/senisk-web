from django.forms import ModelForm

from kioskapp.models import Kiosk


class SelectInforForm(ModelForm):
    class Meta:
        model = Kiosk
        fields = ['type', 'name']