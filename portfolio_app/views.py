from django.shortcuts import render, get_object_or_404
from .models import Projects

# Create your views here.

def index(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')
