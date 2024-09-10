from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin

from petstagram3.core.views_mixins import OwnerRequiredMixin
from petstagram3.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram3.pets.models import Pet


# TODO: change contex object name everywhere

class PetDetailsView(LoginRequiredMixin, views.DetailView):
    queryset = Pet.objects.all() \
        .prefetch_related("petphoto_set")

    template_name = "pets/pet-details-page.html"
    slug_url_kwarg = "pet_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_photos"] = self.object.petphoto_set.all()
        context["total_likes"] = sum([p.photolike_set.count() for p in self.object.petphoto_set.all()])
        return context


class PetCreateView(auth_mixin.LoginRequiredMixin, views.CreateView):
    queryset = Pet.objects.all()
    form_class = PetCreateForm
    template_name = "pets/pet-add-page.html"

    def get_success_url(self):
        return reverse(
            "pet_details",
            kwargs={
                "username": self.object.user.email,
                "pet_slug": self.object.slug,
            }
        )

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user
        return form


class PetEditView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    queryset = Pet.objects.all()
    form_class = PetEditForm
    template_name = "pets/pet-edit-page.html"
    slug_url_kwarg = "pet_slug"

    def get_success_url(self):
        return reverse(
            "pet_details",
            kwargs={
                "username": self.object.user.email,
                "pet_slug": self.object.slug
            }
        )


class PetDeleteView(OwnerRequiredMixin, auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = Pet
    template_name = "pets/pet-delete-page.html"
    context_object_name = "pet"
    success_url = reverse_lazy("index")

    slug_url_kwarg = "pet_slug"

    def get_object(self, queryset=None):
        return Pet.objects.get(slug=self.kwargs["pet_slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PetDeleteForm(initial=self.object.__dict__)
        return context

    def delete(self, request, *args, **kwargs):
        pet = self.get_object()
        pet.delete()
        return redirect(self.success_url)
