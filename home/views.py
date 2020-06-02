from django.shortcuts import render
from django.utils.translation import gettext as _


# Create your views here.
def index(request):
    args= {}
    page_title = _("Bienvenu dans mon Monde")
    args["first_title"] = page_title
    second_title = _("TAROT T")
    args["second_title"] = second_title
    return render(request, 'home/index.html', args)