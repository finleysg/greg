from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    fields = ['name', 'title', 'description', 'beauty_shot', 'active_flag']
    list_display = ["name", "title", "active_flag", ]
    list_filter = ("active_flag", )
    save_on_top = True


admin.site.register(Project, ProjectAdmin)
