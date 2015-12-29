from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^contact/send/$', views.send_message, name='send-message'),
    url(r'^services', views.services, name='services'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^projects/(?P<project_id>[0-9]+)/$', views.project_details, name='project-details'),
]
