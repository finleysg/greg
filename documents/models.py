from django.db import models
from django.db.models import CASCADE
from imagekit import ImageSpec, register
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFit, Transpose

from content.models import Tag
from documents.managers import PhotoManager

DOCUMENT_TYPE_CHOICES = (
    ("TODO", "TODO"),  # Not currently using documents
)


def document_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/documents/year/<filename>
    return "documents/{0}/{1}".format(instance.document_type, filename)


def photo_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/documents/year/<filename>
    return "photos/{0}".format(filename)


class MobileSpec(ImageSpec):
    format = 'JPEG'
    options = {'quality': 80}
    processors = [Transpose(Transpose.AUTO), ResizeToFit(900, 900)]


class WebSpec(ImageSpec):
    format = 'JPEG'
    options = {'quality': 90}
    processors = [Transpose(Transpose.AUTO), ResizeToFit(1600, 1600, upscale=False)]


register.generator("documents:photo:mobile_image", MobileSpec)
register.generator("documents:photo:web_image", WebSpec)


class Document(models.Model):
    document_type = models.CharField(verbose_name="Type", choices=DOCUMENT_TYPE_CHOICES, max_length=16, )
    title = models.CharField(verbose_name="Title", max_length=120)
    file = models.FileField(verbose_name="File", upload_to=document_directory_path, null=True)
    created_by = models.CharField(verbose_name="Created By", max_length=100)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}: {}".format(self.year, self.title)


class Photo(models.Model):
    caption = models.CharField(verbose_name="Caption", max_length=240, null=True, blank=True)
    raw_image = models.ImageField(verbose_name="Image", upload_to=photo_directory_path)
    mobile_image = ImageSpecField(source="raw_image", id="documents:photo:mobile_image")
    web_image = ImageSpecField(source="raw_image", id="documents:photo:web_image")
    created_by = models.CharField(verbose_name="Created By", max_length=100)
    last_update = models.DateTimeField(auto_now=True)

    objects = PhotoManager()

    def __str__(self):
        return "{}: {}".format(self.year, self.caption)


class PhotoTag(models.Model):
    document = models.ForeignKey(verbose_name="Photo", to=Photo, on_delete=CASCADE, related_name="tags")
    tag = models.ForeignKey(verbose_name="Tag", to=Tag, on_delete=CASCADE)
