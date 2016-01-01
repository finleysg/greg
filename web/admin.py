from django.contrib import admin
from .models import Service, Project, ProjectImage, ProjectDescription, SiteSetting, HomePageImage, AboutPage, Message

admin.site.register(SiteSetting)
admin.site.register(Service)
admin.site.register(HomePageImage)
admin.site.register(AboutPage)


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ['from_name', 'message_date']


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
admin.site.register(Message, MessageAdmin)
