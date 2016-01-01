from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^contact/thank-you', views.thanks, name='thanks'),
    url(r'^services', views.services, name='services'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^projects/(?P<slug>[\w-]+)/$', views.project_details, name='project-details'),
]
