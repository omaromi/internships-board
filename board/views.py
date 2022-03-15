from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Staff, Company,Internship
from .forms import IntUpload

# Create your views here.

def home(request):
    context = {
        'jobs': Internship.objects.all(),
        'staff' : Staff.objects.all(),
    }
    return render(request, 'board/home.html', context)

def upload(request):
    form = IntUpload()

    if request.method == 'POST':
        form  = IntUpload(request.Post)
        if form.is_valid():
            form.save()
        # print(request.POST)

    context = {
        'form':form,
    }
    
    return render(request,'board/upload.html', context)