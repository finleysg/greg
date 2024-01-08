from .models import *
from rest_framework import serializers


class PhotoTagSerializer(serializers.ModelSerializer):

    tag = serializers.CharField(source="tag.name")

    class Meta:
        model = PhotoTag
        fields = ("id", "tag", )


class DocumentSerializer(serializers.ModelSerializer):

    created_by = serializers.CharField(read_only=True)
    last_update = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Document
        fields = ("id", "title", "document_type", "file", "created_by", "last_update", )

    def validate(self, data):
        if self.context["request"].method == "PUT" and not data.get("file"):
            data.pop("file", None)
        elif self.context["request"].method == "POST" and not data.get("file"):
            raise Exception("A file is required.")
        return data

    def create(self, validated_data):
        title = validated_data.pop("title")
        document_type = validated_data.pop("document_type")
        file = validated_data.pop("file")
        created_by = self.context["request"].user

        doc = Document(itle=title, document_type=document_type, file=file, created_by=created_by)
        doc.save()

        return doc

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.document_type = validated_data.get("document_type", instance.document_type)
        new_file = validated_data.get("file", None)
        if new_file is not None:
            instance.file = new_file

        instance.save()

        return instance


class PhotoSerializer(serializers.ModelSerializer):

    mobile_url = serializers.ReadOnlyField(source="mobile_image.url")
    web_url = serializers.ReadOnlyField(source="web_image.url")
    image_url = serializers.ReadOnlyField(source="raw_image.url")
    tags = PhotoTagSerializer(many=True, required=False)
    created_by = serializers.CharField(read_only=True)
    last_update = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Photo
        fields = ("id", "caption", "mobile_url", "web_url", "image_url", "raw_image", "created_by", "last_update",
                  "tags", )

    def create(self, validated_data):
        tags = self.context["request"].data.get("tags", None)
        caption = validated_data.get("caption", None)
        raw_image = validated_data.pop("raw_image")
        created_by = self.context["request"].user

        pic = Photo(caption=caption, raw_image=raw_image, created_by=created_by)
        pic.save()

        if tags is not None:
            for tag in tags.split("|"):
                t, created = Tag.objects.get_or_create(name=tag)
                pt = PhotoTag(document=pic, tag=t)
                pt.save()

        return pic

    def update(self, instance, validated_data):
        tags = self.context["request"].data.get("tags", None)

        instance.caption = validated_data.get("caption", instance.caption)
        instance.save()

        # Delete and recreate tags.
        PhotoTag.objects.filter(document=instance).delete()
        if tags is not None:
            for tag in tags:
                t, created = Tag.objects.get_or_create(name=tag.get("name"))
                pt = PhotoTag(document=instance, tag=t)
                pt.save()

        return instance
