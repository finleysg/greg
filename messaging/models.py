from django.db import models


class ContactMessage(models.Model):
    full_name = models.CharField(verbose_name="Full name", max_length=100)
    email = models.CharField(verbose_name="Email", max_length=254)
    message_text = models.TextField(verbose_name="Message text")
    message_date = models.DateTimeField(verbose_name="Message date", auto_now_add=True)

    def __str__(self):
        return self.full_name
