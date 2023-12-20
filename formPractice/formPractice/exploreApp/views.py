from django.shortcuts import render
from .forms import Client

# Create your views here.
def form(request):
    client= Client(request.POST)
    return render(request, 'index.html', {'client': client})
