from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path("create_account/", views.create_account_view, name="create_account"),
    path("logout/", LogoutView.as_view(), name="logout"),    
]