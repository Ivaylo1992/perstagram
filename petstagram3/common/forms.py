from django import forms

from petstagram3.common.models import PhotoComment


class PetPhotoCommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ("text", )
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "placeholder": "Add comment ..."
                }
            )
        }


class SearchForm(forms.Form):
    pet_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by pet name ..."
            }
        )
    )