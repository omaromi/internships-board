from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

jobs = [
    {
        'company':'Amazon',
        'position':'Software Engineer',
        'job_description':'Looking for a entry level fullstack engineer!',
        'date_posted':'February 26, 2022',
    },
    {
        'company':'Netflix',
        'position':'Content Strategist',
        'job_description':'Looking for a junior-year copywriter!',
        'date_posted':'February 23, 2022',
    },
    {
        'company':'Facebook',
        'position':'UX Designer',
        'job_description':'Looking for a UX Designer!',
        'date_posted':'February 26, 2022',
    },
    {
        'company':'CIBC',
        'position':'Business Analyst',
        'job_description':'Looking for a junior-year copywriter!',
        'date_posted':'February 23, 2022',
    },
    {
        'company':'Amazon',
        'position':'Software Engineer',
        'job_description':'Looking for a entry level fullstack engineer!',
        'date_posted':'February 26, 2022',
    },
    {
        'company':'Netflix',
        'position':'Content Strategist',
        'job_description':'Looking for a junior-year copywriter!',
        'date_posted':'February 23, 2022',
    },
]

def home(request):
    context = {
        'jobs': jobs,
    }
    return render(request, 'board/home.html', context)