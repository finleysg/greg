from django.contrib import admin

from core.models import SiteSettings


class SiteSettingsAdmin(admin.ModelAdmin):
    fields = ["home_page_copy", "address_line1", "address_line2", "contact_email", "contact_phone", "contact_us_emails", ]
    list_display = ["address_line1", "address_line2", "contact_email", "contact_phone", ]


admin.site.register(SiteSettings, SiteSettingsAdmin)
