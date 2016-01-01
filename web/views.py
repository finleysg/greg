from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# from django.core.mail import send_mail
from .forms import ContactForm
from .models import HomePageImage, SiteSetting, Project, AboutPage, Service, Message


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
    content = Service.objects.all()
    context = {
        "name": "Services Page",
        "services": content
    }
    return render(request, "web/services.html", context)


def about(request):
    content = AboutPage.objects.first()
    context = {
        "name": "About Us Page",
        "about": content
    }
    return render(request, "web/about.html", context)


def contact(request):
    settings = SiteSetting.objects.first()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/thank-you')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'web/contact.html', {'form': form, 'settings': settings})


def thanks(request):
    settings = SiteSetting.objects.first()
    return render(request, 'web/thanks.html', {'settings': settings})


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