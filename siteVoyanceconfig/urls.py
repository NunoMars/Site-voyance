from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from clairvoyance.views import index, contacts
from django.views.i18n import JavaScriptCatalog
from django.conf import settings


urlpatterns = [
    path("", index, name="home"),
    path('admin', admin.site.urls, name='admin'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path("accounts/", include("accounts.urls"), name="accounts"),
    path('clairvoyance/', include('clairvoyance.urls')),
    path('ball8/', include('ball8.urls')),
    path("contacts", contacts, name="contacts"),
    path('jsi18n/', JavaScriptCatalog.as_view(), name ='javascript-catalog'),    
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]