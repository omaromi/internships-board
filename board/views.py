from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Staff, Company, Internship
from .forms import InternshipForm

# Create your views here.

def home(request):
    context = {
        'jobs': Internship.objects.all(),
        'staff' : Staff.objects.all(),
    }
    return render(request, 'board/home.html', context)

# def upload(request):
#     form = IntUpload()

#     if request.method == 'POST':
#         form  = IntUpload(request.Post)
#         if form.is_valid():
#             form.save()
#         # print(request.POST)

#     context = {
#         'form':form,
#     }
    
#     return render(request,'board/upload.html', context)

def add_internship(request):
    submitted = False
    if request.method == 'POST':
        form = InternshipForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/internshipform?submitted=True')
    else:
        form = InternshipForm
        if 'submitted' in request.GET:
            submitted = True


    context = {
        'form' : form,
        'submitted' : submitted
        }

    return render(request, 'board/internshipform.html', context)