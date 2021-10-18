from django.urls import path

from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'calories_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('addFood/', views.addFood, name='add_food'),
    path('addFoodManual/', views.addFoodManual, name='add_food_manual')
]