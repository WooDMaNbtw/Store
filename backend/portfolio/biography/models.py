from accounts.models import User
from django.db import models
from django.template.defaultfilters import slugify
from rest_framework.reverse import reverse


class Experience(models.Model):
    """
    Work experience model, short description, spent time etc.
    I.e. Self-entrepreneur
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    begin_time = models.DateField()
    end_time = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("biography:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['id']
        verbose_name = "Biography"
        verbose_name_plural = "Biography"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Experience, self).save(*args, **kwargs)


class Information(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    about = models.TextField()
    birth = models.DateField()
    age = models.IntegerField()
    nationality = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=255, default="Male")
    residence = models.CharField(max_length=255, blank=True)
    vkontakte = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.first_name

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['id']
        verbose_name = "Information"
        verbose_name_plural = "Information"
