from django.db import models
from django.db.models import DO_NOTHING

from documents.models import Photo


class Project(models.Model):
    name = models.CharField(verbose_name="Unique project name", max_length=30, unique=True)
    title = models.CharField(verbose_name="Project title", max_length=100)
    description = models.TextField(verbose_name="Project description")
    beauty_shot = models.ForeignKey(verbose_name="Main project picture", to=Photo, related_name="beauty_shot",
                                    on_delete=DO_NOTHING)
    active_flag = models.BooleanField(verbose_name="Show project on the web", default=True)

    def __str__(self):
        return self.name
