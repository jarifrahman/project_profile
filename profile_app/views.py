from django.shortcuts import render

from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects
    return render(request, 'profile_app/home.html',{'jobs':jobs})

