# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Home Page")


def services(request):
    return HttpResponse("Services Page")


def about(request):
    return HttpResponse("About Page")


def contact(request):
    return HttpResponse("Contact Page")


def projects(request):
    return HttpResponse("Projects Page")


def project_details(request, project_id):
    return HttpResponse("Project Page for Project %s" % project_id)