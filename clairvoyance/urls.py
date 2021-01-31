from django.urls import path
from .views import clairvoyance, clairvoyante, history


urlpatterns = [

    path("", clairvoyance, name='clairvoyance'),
    path("clairvoyante/", clairvoyante, name='clairvoyante'),
    path("history/", history, name='history'),
]