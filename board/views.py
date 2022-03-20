from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Staff, Company, Internship
from .forms import InternshipForm, CompanyForm

# Create your views here.

def home(request):
    context = {
        'internships': Internship.objects.all(),
        'staff' : Staff.objects.all(),
    }
    return render(request, 'board/home.html', context)

def add_internship(request):
    submitted = False
    if request.method == 'POST':
        form = InternshipForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_internship?submitted=True')
    else:
        form = InternshipForm
        if 'submitted' in request.GET:
            submitted = True


    context = {
        'form' : form,
        'submitted' : submitted
        }

    return render(request, 'board/add_internship.html', context)

def show_internship(request, internship_id):
    internship = Internship.objects.get(pk=internship_id)
    context = {
        'internship': internship
    }
    return render(request, 'board/show_internship.html', context)

def staffmembers(request):
    # team = 
    context = {
        'staff': Staff.objects.all()
    }
    return render(request, 'board/staff.html', context)

def add_company(request):
    submitted = False
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_company?submitted=True')
    else:
        form = CompanyForm
        if 'submitted' in request.GET:
            submitted = True


    context = {
        'form' : form,
        'submitted' : submitted
        }

    return render(request, 'board/add_company.html', context)

def staff_internships(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)
    internships = staff.internship_set.all()

    context ={
        'staff' : staff,
        'internships': internships,
    }
    return render(request, 'board/staff_internships.html',context)

def update_internship(request, internship_id):
    internship = Internship.objects.get(pk=internship_id)
    form = InternshipForm(request.POST or None, instance=internship)

    if form.is_valid():
        form.save()
        return redirect('show-internship', internship_id)

    context = {
        'internship' : internship,
        'form' : form,
    }
    return render(request, 'board/update_internship.html', context)

def staff_login(request):
    return render(request, 'board/staff_login.html')
