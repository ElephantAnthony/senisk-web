from django.shortcuts import render, redirect
from django.views import View
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

class ChooseUiView(View):
    model = Kiosk
    template_name = 'kioskapp/ui.html'

    def get(self, request):
        selected_ui = request.GET.get('ui')
        user = request.user
        if selected_ui and user.is_authenticated:
            Kiosk.objects.create(user=user, ui=selected_ui)
            return redirect('kioskapp:ui')

    # def choose_ui(self, request, *args, **kwargs):
    #     selected_number = kwargs.get('selected_number')
    #     if request.user.is_authenticated:
    #         user = request.user
    #         Kiosk.objects.create(user=user, ui=selected_number)
    #         return redirect('kioskapp:store_impormation')
    #     else:
    #         return render(request, 'accountapp:login')

