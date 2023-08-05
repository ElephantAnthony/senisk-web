from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView

from kioskapp.forms import KioskCreationForm
from kioskapp.models import Kiosk

class KioskUi(TemplateView):
    template_name = 'kioskapp/ui.html'

class KioskStore(TemplateView):
    template_name = 'kioskapp/Store_information.html'

class KioskColor(TemplateView):
    template_name = 'kioskapp/color.html'

class KioskMenu(TemplateView):
    template_name = 'kioskapp/menu.html'

class KioskDone(TemplateView):
    template_name = 'kioskapp/done.html'

# class KioskMakeView(DetailView):
#     model = Kiosk
#     template_name = 'kioskapp/ui.html'
#
#     def choose_ui(self, request, *args, **kwargs):
#         selected_number = kwargs.get('selected_number')
#         if request.user.is_authenticated:
#             user = request.user
#             Kiosk.objects.create(user=user, ui=selected_number)
#             return redirect('kioskapp:store_impormation')
#         else:
#             return render(request, 'accountapp:login')

