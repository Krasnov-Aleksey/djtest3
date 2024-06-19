from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from .forms import UserRegisterForm, UserLoginForm, CategoryForm, RecipesForm


def index(request):
    return render(request, 'djtest3app/index.html')


def recipe_category(request):
    return render(request, 'djtest3app/recipe_category.html')


def list_recipe(request):
    return render(request, 'djtest3app/list_recipe.html')


def add_recipe(request):
    return render(request, 'djtest3app/add_recipe.html')


class UserLogoutView(LogoutView):
    """
    Выход с сайта
    """
    next_page = 'index'


class UserRegisterView(SuccessMessageMixin, CreateView):
    """
    Представление регистрации на сайте с формой регистрации
    """
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')
    template_name = 'djtest3app/user_register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context


class UserLoginView(SuccessMessageMixin, LoginView):
    """
    Авторизация на сайте
    """
    form_class = UserLoginForm
    template_name = 'djtest3app/user_login.html'
    next_page = 'index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context
