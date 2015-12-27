"""
Definition of models.
"""
from django.db import models


def generate_foldername(self, filename):
    url = "projects/%s/%s" % (self.slug, filename)
    return url


class Site(models.Model):
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)


class Service(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30)
    title = models.CharField(max_length=100)
    service = models.ForeignKey(Service)
    main_category = models.CharField(max_length=60)
    tag_list = models.CharField(max_length=100, blank=True)
    beauty_shot = models.ImageField(upload_to=generate_foldername)
    active_flag = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProjectDescription(models.Model):
    project = models.ForeignKey(Project)
    paragraph = models.TextField()


class ProjectImage(models.Model):
    project = models.ForeignKey(Project)
    image = models.ImageField()

