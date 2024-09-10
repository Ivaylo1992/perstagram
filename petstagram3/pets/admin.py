from django.contrib import admin

from petstagram3.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
