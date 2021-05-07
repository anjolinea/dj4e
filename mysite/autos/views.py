from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from autos.models import Auto, Make


# front page... autos/
class MainView(LoginRequiredMixin, View):
    def get(self, request):
        template_name = 'autos/auto_list.html'
        # info needed: list of autos and the make count
        auto_list = Auto.objects.all()
        make_count = Make.objects.all().count()

        # give them a key-value pair for template
        ctx = {'make_count': make_count, 'auto_list': auto_list}

        # return view
        return render(request, template_name, ctx)


# make list page... autos/lookup/
class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        template_name = 'autos/make_list.html'
        # info needed: list of makes
        make_list = Make.objects.all()
        ctx = {'make_list': make_list}
        return render(request, template_name, ctx)


# Make Section: Add, Update, Delete


class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


# Auto Section: Add, Update, Delete

class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')