from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = { "name": "Home Page" }
    return render(request, "web/index.html", context)


def services(request):
    return HttpResponse("Services Page")


def about(request):
    return HttpResponse("About Page")


def contact(request):
    context = { "name": "Contact Page" }
    return render(request, "web/contact.html", context)


def send_message(request):
    return HttpResponse("We heard you say %s" % request.POST["message"])


def projects(request):
    return HttpResponse("Projects Page")


def project_details(request, project_id):
    return HttpResponse("Project Page for Project %s" % project_id)