from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms

from petstagram3.accounts.models import Profile

UserModel = get_user_model()


class PetstagramUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ("email", )


class PetstagramUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class PetstagramUserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.TextInput(attrs={"autofocus": True})
    )

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password"}
        )
    )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "date_of_birth", "profile_picture", "gender"]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "date_of_birth": "Date of Birth",
            "profile_picture": "Profile Picture",
            "gender": "Gender",
        }

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "First Name"
                }),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Last Name"
                }
            ),
            "date_of_birth": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
            "profile_picture": forms.URLInput(
                attrs={
                    "placeholder": "Profile Picture URL"
                }
            )
        }


# TODO: Create a profile delete form