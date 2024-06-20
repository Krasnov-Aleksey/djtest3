from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe_category/', views.recipe_category, name='recipe_category'),
    path('list_recipe/', views.list_recipe, name='list_recipe'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('success/', views.Success.as_view(), name='success'),
    path('recipe/<int:recipe_id>/', views.recipe, name='recipe'),
    path('update_recipe/<int:recipe_id>/', views.update_recipe, name='update_recipe'),
    path('recipe_read/<int:recipe_id>/', views.recipe_read, name='recipe_read'),
    path('recipe_in_category/<int:category_id>/', views.recipe_in_category, name='recipe_in_category'),

]

urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
                + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
