from django import forms

from petstagram3.core.form_mixins import ReadonlyFieldsMixin
from petstagram3.pets.models import Pet
from petstagram3.photos.models import PetPhoto


class PetPhotoCreateForm(forms.ModelForm):

    class Meta:
        model = PetPhoto
        fields = "__all__"
        exclude = ("user", )


class PetPhotoEditForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        exclude = ("user", "photo")


class PetPhotoDeleteForm(ReadonlyFieldsMixin, forms.ModelForm):
    readonly_fields = "__all__"

    class Meta:
        model = PetPhoto
        exclude = ("user", )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance