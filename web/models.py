"""
Definition of models.
"""
from django.db import models


def generate_foldername(self, filename):
    url = "projects/%s/%s" % (self.name.lower().replace(" ", "_"), filename)
    return url


def generate_detail_foldername(self, filename):
    url = "projects/%s/%s" % (self.project.name.lower().replace(" ", "_"), filename)
    return url


class HomePageImage(models.Model):
    carousel_image = models.ImageField(verbose_name="Carousel Image", upload_to="home")
    caption = models.CharField(verbose_name="Image Caption", max_length=100)

    def __str__(self):
        return self.caption


class AboutPage(models.Model):
    about_image = models.ImageField(verbose_name="About page main image", upload_to="home")
    paragraph1 = models.TextField()
    paragraph2 = models.TextField(blank=True)
    paragraph3 = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "About page"


class SiteSetting(models.Model):
    home_page_copy = models.TextField(verbose_name="Home page main text")
    address_line1 = models.CharField(verbose_name="Address (first line)", max_length=40)
    address_line2 = models.CharField(verbose_name="Address (second line)", max_length=40)
    contact_email = models.EmailField(verbose_name="Public email address", blank=True)
    contact_phone = models.CharField(verbose_name="Public phone number", blank=True, max_length=15)
    posted_hours = models.CharField(verbose_name="Public posted hours", blank=True, max_length=60)
    facebook_address = models.CharField(verbose_name="Public Facebook page", blank=True, max_length=100)
    linkedin_address = models.CharField(verbose_name="Public Linked-In page", blank=True, max_length=100)
    twitter_address = models.CharField(verbose_name="Public Twitter address", blank=True, max_length=100)


class Message(models.Model):
    from_name = models.CharField(verbose_name="Full Name", max_length=100)
    from_phone = models.CharField(verbose_name="Phone Number", max_length=20)
    from_email = models.EmailField(verbose_name="Email Address")
    message_text = models.TextField(verbose_name="Message")
    message_date = models.DateTimeField(verbose_name="Message date", auto_now=True)


class Service(models.Model):
    title = models.CharField(verbose_name="Service title", max_length=100, unique=True)
    description = models.TextField(verbose_name="Service description")

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(verbose_name="Unique project name", max_length=30, unique=True)
    slug = models.SlugField(max_length=30)
    title = models.CharField(verbose_name="Project title", max_length=100)
    # service = models.ForeignKey(Service)
    beauty_shot = models.ImageField(verbose_name="Main project picture", upload_to=generate_foldername)
    active_flag = models.BooleanField(verbose_name="Show project on the web", default=True)

    def save(self, *args, **kwargs):
        self.slug = self.name.lower().replace(" ", "-")
        super(Project, self).save(*args, **kwargs) # Call the "real" save() method.

    @property
    def description(self):
        child = self.projectdescription_set.first()
        if child is not None:
            return child.paragraph
        return ""

    def __str__(self):
        return self.name


class ProjectDescription(models.Model):
    project = models.ForeignKey(Project)
    paragraph = models.TextField(verbose_name="Project description paragraph")


class ProjectImage(models.Model):
    project = models.ForeignKey(Project)
    image = models.ImageField(verbose_name="Project detail picture", upload_to=generate_detail_foldername)

