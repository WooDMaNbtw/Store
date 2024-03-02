from django.contrib import admin
from .models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'position',
        'company',
        'title',
        'description',
    )
