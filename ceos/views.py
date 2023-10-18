from django.shortcuts import render
from ceos.models import CeosUpdate


# Create your views here.
def index(request):
    all_ceos = CeosUpdate.objects.all()
    ceos_length = len(all_ceos)
    context = {"all_ceos": all_ceos, "ceos_length": ceos_length}
    return render(request, "index.html", context)
