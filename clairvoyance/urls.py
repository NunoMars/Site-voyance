from django.urls import path
from . import views


urlpatterns = [
    path("", views.clairvoyance, name='clairvoyance'),
    path("", views.clairvoyante, name='clairvoyante'),
]