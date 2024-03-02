from django.contrib.auth.models import User
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

