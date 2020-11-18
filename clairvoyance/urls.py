from django.urls import path
from .views import clairvoyance, clairvoyante, index, history


urlpatterns = [
    path("", index, name='home'),
    path("clairvoyance", clairvoyance, name='clairvoyance'),
    path("clairvoyante/", clairvoyante, name='clairvoyante'),
    path("history/", history, name='history'),
]