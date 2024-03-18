from django.db import models
from rest_framework.reverse import reverse
from biography.models import Experience


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Project(models.Model):
    """ I.e. Parsite """
    experience = models.ForeignKey(Experience, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    link = models.URLField(default=None)
    description = models.TextField()
    image = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field"
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    draft = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"id": self.id})

    class Meta:
        ordering = ['id']
        verbose_name = "Project"
        verbose_name_plural = "Projects"
