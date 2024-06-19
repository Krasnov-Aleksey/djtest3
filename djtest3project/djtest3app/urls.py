from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe_category/', views.recipe_category, name='recipe_category'),
    path('list_recipe/', views.list_recipe, name='list_recipe'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
]
