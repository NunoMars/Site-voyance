from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import clairvoyance, clairvoyante, history, csrf_failure


urlpatterns = [
    path("", clairvoyance, name='clairvoyance'),
    url("clairvoyante", csrf_exempt(clairvoyante), name='clairvoyante'),
    path("history", history, name='history'),
    path("csrf_failure", csrf_failure, name='csrf_failure'),
]