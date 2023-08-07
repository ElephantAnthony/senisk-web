from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, TemplateView

from kioskapp.forms import SelectInforForm
from kioskapp.models import Kiosk


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
        user = request.user

        if user.is_authenticated and ui:
            print('이미지 클릭')
            print(ui)
            kiosk, created = Kiosk.objects.get_or_create(user=user)
            kiosk.ui = ui
            kiosk.save()
            return redirect('kioskapp:select_ui')

        return render(request, self.template_name)

class SelectInforView(View):
    model = Kiosk
    form_class = SelectInforForm
    template_name = 'kioskapp/store_information.html'

    def get(self, request):
        user_kiosk = Kiosk.objects.get(user=request.user)
        initial_data = {'type': user_kiosk.type, 'name': user_kiosk.name}
        form = self.form_class(initial=initial_data)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user_kiosk, created = Kiosk.objects.get_or_create(user=request.user)
            user_kiosk.type = form.cleaned_data['type']
            user_kiosk.name = form.cleaned_data['name']
            user_kiosk.save()
            return redirect('success_page')

        return render(request, self.template_name, {'form': form})

    # def get(self, request):
    #     form = self.form_class()
    #     return render(request, self.template_name, {'form': form})
    #
    # def post(self, request):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         temp_infor = form.save(commit=False)
    #         target_kiosk, created = Kiosk.objects.get(user=request.user)
    #         temp_infor.type = target_kiosk
    #         temp_infor.user = self.request.user
    #         temp_infor.save()
    #         return redirect('success_page')
    #
    #     return render(request, self.template_name, {'form': form})





