from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from cats.models import Cat, Breed

# front page... cats/
class MainView(LoginRequiredMixin, View):
    def get(self, request):
        template_name = 'cats/cat_list.html'
        # info needed: list of cats and the breed count
        cat_list = Cat.objects.all()
        breed_count = Breed.objects.all().count()

        # give them a key-value pair for template
        ctx = {'breed_count': breed_count, 'cat_list': cat_list}

        # return view
        return render(request, template_name, ctx)


# breed list page... cats/lookup/
class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        template_name = 'cats/breed_list.html'
        # info needed: list of breeds
        breed_list = Breed.objects.all()
        ctx = {'breed_list': breed_list}
        return render(request, template_name, ctx)


# Breed Section: Create, Update, Delete


class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


# Cat Section: Create, Update, Delete

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')