from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from petstagram3.accounts.forms import PetstagramUserCreationForm, PetstagramUserLoginForm, ProfileEditForm
from petstagram3.accounts.models import Profile
from petstagram3.core.views_mixins import OwnerRequiredMixin

UserModel = get_user_model()


class PetstagramUserRegisterView(views.CreateView):
    model = UserModel
    form_class = PetstagramUserCreationForm
    template_name = "accounts/register-page.html"
    success_url = reverse_lazy("login")


class PetstagramUserLoginView(auth_views.LoginView):
    form_class = PetstagramUserLoginForm
    template_name = "accounts/login-page.html"

    def form_valid(self, form):
        super().form_valid(form)
        profile_instance, _ = Profile.objects.get_or_create(user=self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class PetstagramUserLogoutView(auth_views.LogoutView):
    ...


class PetstagramUserEditView(OwnerRequiredMixin, LoginRequiredMixin, views.UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = "accounts/profile-edit-page.html"

    def get_success_url(self):
        return reverse_lazy(
            "profile_details",
            kwargs={
                "pk": self.object.pk
            }
        )


class ProfileDetailsView(views.DetailView):
    queryset = Profile.objects.all() \
        .prefetch_related("user")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_likes = sum([
            p.photolike_set.count() for p in self.object.user.petphoto_set.all()
        ])
        context["total_likes"] = total_likes
        return context

    template_name = "accounts/profile-details-page.html"


# TODO: Create a profile delete view

class PetstagramUserDeleteView(OwnerRequiredMixin, LoginRequiredMixin, views.DeleteView):
    model = UserModel
    template_name = "accounts/profile-delete-page.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.success_url)
