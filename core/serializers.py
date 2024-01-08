from rest_framework import serializers
from .models import SiteSettings


class SiteSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteSettings
        fields = ("id", "home_page_copy", "address_line1", "address_line2", "contact_email", "contact_phone",
                  "contact_us_emails", )
