from petstagram3.photos.models import PetPhoto

PET_PHOTO_DATA = {
    "photo": "photo.jpg",
    "description": "Test description",
    "location": "Sofia",
}


def create_valid_pet_photo(user, tagged_pets):
    photo = PetPhoto(
        **PET_PHOTO_DATA,
        user=user,
    )

    photo.save()
    photo.tagged_pets.add(tagged_pets)
    photo.save()
    return photo