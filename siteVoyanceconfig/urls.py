from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views
from clairvoyance.views import index


urlpatterns = [
    url(r"^$", index, name="index"),
    path('admin/', admin.site.urls),
    path(r"accounts/", include("django.contrib.auth.urls")),
    path(r"accounts/", include("accounts.urls"), name="accounts"),
    path('clairvoyance', include('clairvoyance.urls')),
    path('ball8', include('ball8.urls'))

]
