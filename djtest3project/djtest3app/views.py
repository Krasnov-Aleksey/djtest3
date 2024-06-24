from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from .forms import UserRegisterForm, UserLoginForm, CategoryForm, RecipesForm
from .models import Category, Recipes
from random import choice


def index(request):
    quantity_recipes_index = 5
    recipes = Recipes.objects.all()
    recipe_list = []
    recipe_rnd = []
    if len(recipes) > quantity_recipes_index:
        for item in recipes:
            recipe_list.append(item)

        for _ in range(quantity_recipes_index):
            rnd = choice(recipe_list)
            recipe_rnd.append(rnd)
            index_rnd = recipe_list.index(rnd)
            recipe_list.pop(index_rnd)
    else:
        for item in recipes:
            recipe_rnd.append(item)

    return render(request, 'djtest3app/index.html', {'recipes': recipe_rnd})


def recipe_category(request):
    categorys = Category.objects.all()
    return render(request, 'djtest3app/recipe_category.html', {'categorys': categorys})


def list_recipe(request):
    current_user = request.user
    recipes = Recipes.objects.filter(author_recipe=current_user)
    return render(request, 'djtest3app/list_recipe.html', {'recipes': recipes})


def add_recipe(request):
    current_user = request.user
    if request.method == 'POST':
        form = RecipesForm(request.POST, request.FILES, initial={
            "author_recipe": current_user})
        if form.is_valid():
            form.save()
            return render(request, 'djtest3app/success.html')
    else:
        form = RecipesForm(initial={"author_recipe": current_user})

    return render(request, 'djtest3app/add_recipe.html',
                  {'form': form, 'current_user': current_user})


def update_recipe(request, recipe_id):
    recipe = Recipes.objects.get(pk=recipe_id)
    if request.method == 'POST':
        form = RecipesForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return render(request, 'djtest3app/success.html')

    else:
        form = RecipesForm(instance=recipe)
        context = {'form': form}
        return render(request, 'djtest3app/update_recipe.html', context)


def recipe(request, recipe_id):
    recipe = Recipes.objects.get(pk=recipe_id)
    return render(request, 'djtest3app/recipe.html', {'recipe': recipe})


def recipe_read(request, recipe_id=2):
    recipe = Recipes.objects.get(pk=recipe_id)
    return render(request, 'djtest3app/recipe_read.html', {'recipe': recipe})


def recipe_in_category(request, category_id):
    recipes = Recipes.objects.filter(recipes_category=category_id)
    return render(request, 'djtest3app/recipe_in_category.html', {'recipes': recipes})


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


class Success(TemplateView):
    # Страница успешного действия
    template_name = 'djtest3app/success.html'
