from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


def index(request):
    return render(request, 'djtest3app/index.html')


def recipe_category(request):
    return render(request, 'djtest3app/recipe_category.html')


def list_recipe(request):
    return render(request, 'djtest3app/list_recipe.html')


def add_recipe(request):
    return render(request, 'djtest3app/add_recipe.html')


class UserLogoutView(TemplateView):
    next_page = 'index'


class UserRegisterView(TemplateView):
    template_name = 'djtest3app/user_register.html'


class UserLoginView(TemplateView):
    """
    Авторизация на сайте
    """
    template_name = 'djtest3app/user_login.html'
