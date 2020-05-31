from django.shortcuts import render

# Create your views here.
def clairvoyance(request):
    return render(request, 'clairvoyance/index.html')