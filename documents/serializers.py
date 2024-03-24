from .models import *
from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):

    mobile_url = serializers.ReadOnlyField(source="mobile_image.url")
    web_url = serializers.ReadOnlyField(source="web_image.url")
    image_url = serializers.ReadOnlyField(source="raw_image.url")
    created_by = serializers.CharField(read_only=True)
    last_update = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Photo
        fields = ("id", "caption", "mobile_url", "web_url", "image_url", "raw_image", "created_by", "last_update",
                  "category", )

    def create(self, validated_data):
        category = validated_data.get("category", None)
        caption = validated_data.get("caption", None)
        raw_image = validated_data.pop("raw_image")
        created_by = self.context["request"].user

        pic = Photo(category=category, caption=caption, raw_image=raw_image, created_by=created_by)
        pic.save()
        return pic

    def update(self, instance, validated_data):

        instance.caption = validated_data.get("caption", instance.caption)
        instance.category = validated_data.get("category", instance.caption)
        instance.save()

        return instance
