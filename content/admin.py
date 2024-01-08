from django.contrib import admin
from .models import PageContent, Tag


class PageContentAdmin(admin.ModelAdmin):
    fields = ['key', 'title', 'content', ]
    list_display = ['key', 'title', ]
    list_filter = ('key',)
    save_on_top = True


class TagAdmin(admin.ModelAdmin):
    fields = ["name", ]
    list_display = ["name", ]


admin.site.register(PageContent, PageContentAdmin)
admin.site.register(Tag, TagAdmin)
