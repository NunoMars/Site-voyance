from django.urls import path
from .views import clairvoyance, clairvoyante


urlpatterns = [
    path("", clairvoyance, name='clairvoyance'),
    path("", clairvoyante, name='clairvoyante'),
]