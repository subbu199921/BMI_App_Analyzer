from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.upload, name='upload'),  # BMI Upload Page
    path('register/', views.register, name='register'),  # Register Page
    path('login/', auth_views.LoginView.as_view(template_name='ageapp/login.html'), name='login'),  # Login Page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout-get/', LogoutView.as_view(), name='logout_get'),
]
