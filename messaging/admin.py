from django.contrib import admin

from .models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": ("full_name", "email", )
        }),
        ("Message", {
            "fields": ("message_text", )
        }),
    )
    list_display = ["full_name", "message_date", ]
    list_filter = ("message_date", )
    save_on_top = True


admin.site.register(ContactMessage, ContactMessageAdmin)
