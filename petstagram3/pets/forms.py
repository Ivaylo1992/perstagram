from django import forms

from petstagram3.core.form_mixins import ReadonlyFieldsMixin
from petstagram3.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["name", "date_of_birth", "personal_photo"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Pet Name"
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'YYYY-MM-DD',
                    'type': 'date',
                }
            ),
            "personal_photo": forms.URLInput(
                attrs={
                    "placeholder": "Photo URL",
                }
            )
        }

        labels = {
            "name": "Pet Name",
            "personal_photo": "Link to Image"
        }


class PetCreateForm(PetBaseForm):
    ...


class PetEditForm(ReadonlyFieldsMixin, PetBaseForm):
    readonly_fields = ("date_of_birth", )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    def clean_date_of_birth(self):
        return self.instance.date_of_birth


class PetDeleteForm(ReadonlyFieldsMixin, PetBaseForm):
    readonly_fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance