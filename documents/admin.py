from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    fields = ["category", "caption", "raw_image", "created_by", "last_update", ]
    readonly_fields = ("image_preview", "created_by", "last_update",)
    list_display = ["created_by", "category", "image_preview", "caption", "last_update", ]
    list_editable = ["category", "caption", ]
    save_on_top = True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()

    def image_preview(self, obj):
        return mark_safe('<img src="{url}" width="200" />'.format(url=obj.raw_image.url))


admin.site.register(Photo, PhotoAdmin)
