from django.contrib import admin

from petstagram3.photos.models import PetPhoto


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ["pk", "description", "date_of_publication", "get_tagged_pets", "user_profile_names"]

    @staticmethod
    def get_tagged_pets(obj):
        return ", ".join(p.name for p in obj.tagged_pets.all())

    @staticmethod
    def user_profile_names(obj):
        return obj.user.profile.get_full_name()