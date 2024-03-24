from django.contrib.auth.models import User

from rest_framework import serializers
from .models import SiteSettings


class SiteSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteSettings
        fields = ("id", "home_page_copy", "address_line1", "address_line2", "contact_email", "contact_phone",
                  "contact_us_emails", )


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email",
                  "is_authenticated", "is_staff", "is_active", )
        read_only_fields = ("id", "is_authenticated", "is_staff", "is_active", )
