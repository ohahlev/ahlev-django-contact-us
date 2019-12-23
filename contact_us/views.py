from django.shortcuts import render, get_list_or_404
from .models import Contact

def index(request):
    contacts = get_list_or_404(Contact)
    context = {
        'contact': contacts[0],
    }
    return render(request, 'contact_us/index.html', context=context)