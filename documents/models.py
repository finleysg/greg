from django.db import models
from imagekit import ImageSpec, register
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFit, Transpose


def photo_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/photos/<filename>
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


class Photo(models.Model):
    caption = models.CharField(verbose_name="Caption", max_length=240, null=True, blank=True)
    category = models.CharField(verbose_name="Category", max_length=20, null=True, blank=True)
    raw_image = models.ImageField(verbose_name="Image", upload_to=photo_directory_path)
    mobile_image = ImageSpecField(source="raw_image", id="documents:photo:mobile_image")
    web_image = ImageSpecField(source="raw_image", id="documents:photo:web_image")
    created_by = models.CharField(verbose_name="Created By", max_length=100)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}: {}".format(self.category, self.raw_image)
