from django.shortcuts import render
from . models import *
from .forms import contactForm
# Create your views here.

def HomePage(request):

    projects = Projects.objects.all()
    context = {'projects':projects}
    return render(request,'blog/home.html',context)


def projects_list(request):
    projects = Projects.objects.all()
    context = {'projects':projects}
    return render(request,'blog/projects.html',context)


def singleProject(request,pk):
    project = Projects.objects.get(pk=pk)
    tags = project.tags.all()
    context={'project':project,'tags':tags}
    return render(request,'blog/single-project.html',context)


def contactPage(request):
    page = 'Keep in touch with me'
    context = {'page':page}

    return render(request,'blog/contact-form.html',context)


def sendMessage(request):
    form = contactForm()
    context= {'form':form}
    return render(request,'blog/contact-form.html',context)


def showSKills(request):
    skills = Skills.objects.all()
    context = {'skills':skills}
    return render(request,'blog/home.html',context)