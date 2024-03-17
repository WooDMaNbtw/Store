from django.contrib import admin
from .models import Experience, Information


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'position',
        'company',
        'title',
        'description',
    )


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'age'
    )


