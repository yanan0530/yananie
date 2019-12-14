from django.shortcuts import render
from .models import Topmenu


# Create your views here.
def index(request):
    topmenu = Topmenu.objects.all()
    context = {'topmenu': topmenu}
    return render(request, 'index.html', context)
