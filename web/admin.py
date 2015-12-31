from django.contrib import admin
from .models import Service, Project, ProjectImage, ProjectDescription, SiteSetting, HomePageImage

admin.site.register(SiteSetting)
admin.site.register(Service)
admin.site.register(HomePageImage)


class DescriptionInline(admin.StackedInline):
    model = ProjectDescription
    extra = 3


class ImageInline(admin.StackedInline):
    model = ProjectImage
    extra = 5


class ProjectAdmin(admin.ModelAdmin):
    fields = ['name', 'title', 'beauty_shot', 'active_flag']
    inlines = [DescriptionInline, ImageInline]

admin.site.register(Project, ProjectAdmin)