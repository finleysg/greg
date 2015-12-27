from django.contrib import admin
from .models import Service, Project, ProjectImage, ProjectDescription, Site

admin.site.register(Site)
admin.site.register(Service)


class DescriptionInline(admin.StackedInline):
    model = ProjectDescription
    extra = 4


class ImageInline(admin.StackedInline):
    model = ProjectImage
    extra = 7


class ProjectAdmin(admin.ModelAdmin):
    inlines = [DescriptionInline, ImageInline]

admin.site.register(Project, ProjectAdmin)