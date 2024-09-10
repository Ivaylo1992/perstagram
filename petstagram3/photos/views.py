from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

from django.views import generic as views

from petstagram3.common.forms import PetPhotoCommentForm
from petstagram3.core.views_mixins import OwnerRequiredMixin
from petstagram3.photos.forms import PetPhotoCreateForm, PetPhotoEditForm, PetPhotoDeleteForm
from petstagram3.photos.models import PetPhoto


class PetPhotoDetailsView(LoginRequiredMixin, views.DetailView):
    queryset = PetPhoto.objects.all()\
        .prefetch_related("photocomment_set")\
        .prefetch_related("photolike_set")

    context_object_name = "photo"

    template_name = "photos/photo-details-page.html"

    extra_context = {
        "comment_form": PetPhotoCommentForm
    }


class PetPhotoCreateView(LoginRequiredMixin, views.CreateView):
    queryset = PetPhoto.objects.all().prefetch_related("tagged_pets")
    template_name = "photos/photo-add-page.html"
    form_class = PetPhotoCreateForm

    def get_success_url(self):
        return reverse(
            "photo_details",
            kwargs={
                "pk": self.object.pk
            }
        )

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.instance.user = self.request.user
        return form


class PetPhotoEditView(OwnerRequiredMixin, views.UpdateView):
    queryset = PetPhoto.objects.all()
    template_name = "photos/photo-edit-page.html"
    form_class = PetPhotoEditForm

    def get_success_url(self):
        return reverse(
            "photo_details",
            kwargs={
                "pk": self.object.pk
            }
        )


class PetPhotoDeleteView(OwnerRequiredMixin, LoginRequiredMixin, views.DeleteView):
    model = PetPhoto
    template_name = "photos/photo-delete-page.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PetPhotoDeleteForm(initial=self.object.__dict__)
        return context

    def delete(self, request, *args, **kwargs):
        photo = self.get_object()
        photo.delete()
        return redirect(self.success_url)