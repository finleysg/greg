from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Document, PhotoTag, Photo


class PhotoTagInline(admin.TabularInline):
    model = PhotoTag
    can_delete = True
    extra = 0


class DocumentAdmin(admin.ModelAdmin):
    fields = ["title", "document_type", "file", "created_by", "last_update", ]
    readonly_fields = ("created_by", "last_update",)
    exclude = ("tags",)
    list_display = ["title", "document_type", "last_update", ]
    list_filter = ("document_type", )
    save_on_top = True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()


class PhotoAdmin(admin.ModelAdmin):
    fields = ["caption", "raw_image", "created_by", "last_update", ]
    readonly_fields = ("image_preview", "created_by", "last_update",)
    inlines = [PhotoTagInline, ]
    list_display = ["caption", "image_preview", "created_by", "last_update", ]
    # list_filter = ("year",) TODO: filter by tags
    save_on_top = True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()

    def image_preview(self, obj):
        return mark_safe('<img src="{url}" width="200" />'.format(url=obj.raw_image.url))


admin.site.register(Document, DocumentAdmin)
admin.site.register(Photo, PhotoAdmin)
