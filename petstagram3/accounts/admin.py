from django.contrib import admin
from django.contrib.auth import get_user_model

from petstagram3.accounts.forms import PetstagramUserChangeForm, PetstagramUserCreationForm
from petstagram3.accounts.models import PetstagramUser

UserModel = get_user_model()


@admin.register(PetstagramUser)
class PetstagramUserAdmin(admin.ModelAdmin):
    model = UserModel
    add_form = PetstagramUserCreationForm
    form = PetstagramUserChangeForm

    list_display = ("pk", "email", "is_staff", "is_superuser",)
    search_fields = ("email",)
    ordering = ("pk",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ()}),
        ("Permissions", {"fields": ("is_active", "is_staff", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            }
        )
    )
