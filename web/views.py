from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = { "name": "Home Page" }
    return render(request, "web/index.html", context)


def services(request):
    context = { "name": "Services Page" }
    return render(request, "web/services.html", context)


def about(request):
    context = { "name": "About Us Page" }
    return render(request, "web/about.html", context)


def contact(request):
    context = { "name": "Contact Page" }
    return render(request, "web/contact.html", context)


def send_message(request):
    return HttpResponse("We heard you say %s" % request.POST["message"])


def projects(request):
    context = { "name": "Projects Page" }
    return render(request, "web/projects.html", context)


def project_details(request, project_id):
    context = { "name": "Project Detail Page" }
    return render(request, "web/project.html", context)
    # return HttpResponse("Project Page for Project %s" % project_id)