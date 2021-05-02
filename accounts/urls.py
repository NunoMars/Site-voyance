from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("create_account/", views.create_account_view, name="create_account"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("email_change/", views.email_change, name="email_change"),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),    
]