from django.db import models


class SiteSettings(models.Model):
    home_page_copy = models.TextField(verbose_name="Home page main text")
    address_line1 = models.CharField(verbose_name="Address (first line)", max_length=60)
    address_line2 = models.CharField(verbose_name="Address (second line)", max_length=60)
    contact_email = models.EmailField(verbose_name="Public email address")
    contact_phone = models.CharField(verbose_name="Public phone number", null=True, blank=True, max_length=15)
    contact_us_emails = models.CharField(verbose_name="Contact us emails", max_length=400)

    def __str__(self):
        return "Site Settings"

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
