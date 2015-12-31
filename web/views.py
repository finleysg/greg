from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import HomePageImage, SiteSetting, Project, ProjectDescription


# Create your views here.
def index(request):
    images = HomePageImage.objects.all()
    settings = SiteSetting.objects.first()
    context = {
        "name": "Home Page",
        "featureText": settings.home_page_copy,
        "images": images
    }
    return render(request, "web/index.html", context)


def services(request):
    context = { "name": "Services Page" }
    return render(request, "web/services.html", context)


def about(request):
    context = { "name": "About Us Page" }
    return render(request, "web/about.html", context)


def contact(request):
    settings = SiteSetting.objects.first()
    context = {
        "name": "Contact Page",
        "settings": settings
    }
    return render(request, "web/contact.html", context)


def send_message(request):
    return HttpResponse("We heard you say %s" % request.POST["message"])


def projects(request):
    active_projects = Project.objects.filter(active_flag=True)
    context = {
        "name": "Projects Page",
        "projects": active_projects
    }
    return render(request, "web/projects.html", context)


def project_details(request, slug):
    this_project = get_object_or_404(Project, slug=slug)
    descriptions = this_project.projectdescription_set.all()
    images = this_project.projectimage_set.all()
    context = {
        "name": "Project Detail Page",
        "project": this_project,
        "descriptions": descriptions,
        "images": images
    }
    return render(request, "web/project.html", context)