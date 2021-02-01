from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from clairvoyance.views import index


urlpatterns = [
    path("", index, name="home"),
    path('admin', admin.site.urls, name='admin'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls"), name="accounts"),
    path('clairvoyance/', include('clairvoyance.urls')),
    path('ball8/', include('ball8.urls'))

]
