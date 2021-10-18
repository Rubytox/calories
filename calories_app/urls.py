from django.urls import path

from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'calories_app'
urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('addFood/', views.AddFoodView.as_view(), name='add_food'),
    path('addFoodManual/', views.AddFoodManualView.as_view(), name='add_food_manual')
]