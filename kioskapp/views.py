from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, TemplateView

from kioskapp.forms import KioskCreationForm
from kioskapp.models import Kiosk

# class KioskStore(TemplateView):
#     template_name = 'kioskapp/Store_information.html'
#
# class KioskColor(TemplateView):
#     template_name = 'kioskapp/color.html'
#
# class KioskMenu(TemplateView):
#     template_name = 'kioskapp/menu.html'
#
# class KioskDone(TemplateView):
#     template_name = 'kioskapp/done.html'

class SelectSaveUIView(View):
    model = Kiosk
    template_name = 'kioskapp/ui.html'

    def get(self, request, ui=None):
        print('get')
        user = request.user
        print('user')

        if user.is_authenticated and ui:
            print('이미지 클릭')
            print(ui)
            kiosk, created = Kiosk.objects.get_or_create(user=user)
            kiosk.ui = ui
            kiosk.save()
            return redirect('kioskapp:select_ui')

        return render(request, self.template_name)


