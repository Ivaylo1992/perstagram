from django.shortcuts import redirect, resolve_url
from pyperclip import copy
from django.views import generic as views
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from petstagram3.common.forms import PetPhotoCommentForm, SearchForm
from petstagram3.common.models import PhotoLike
from petstagram3.photos.models import PetPhoto


class IndexView(views.ListView):
    model = PetPhoto
    search_form = SearchForm
    comment_form = PetPhotoCommentForm
    context_object_name = "all_photos"

    template_name = "common/home-page.html"

    def get_paginate_by(self, queryset):
        return 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=self.queryset, **kwargs)
        context["comment_form"] = self.comment_form
        context["search_form"] = self.search_form
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pet_name = self.request.GET.get("pet_name")

        if pet_name:
            self.request.session["pet_name"] = pet_name
        else:
            self.request.session.pop("pet_name", None)

        pet_name_session = self.request.session.get("pet_name")

        if pet_name:
            queryset = queryset.filter(tagged_pets__name__icontains=pet_name_session)

        return queryset


def like_functionality(request, photo_id):
    photo = PetPhoto.objects.get(id=photo_id)
    try:
        like = PhotoLike.objects \
            .filter(
            to_photo_id=photo_id,
            user=request.user) \
            .first()
    except TypeError:
        return redirect("login")

    if like:
        like.delete()
    else:
        like = PhotoLike(to_photo=photo, user=request.user)
        like.save()

    return redirect(request.META["HTTP_REFERER"] + f"#{photo_id}")


def copy_link_to_clipboard(request, photo_id):
    copy(request.META["HTTP_HOST"] + resolve_url("photo_details", photo_id))
    return redirect(request.META["HTTP_REFERER"] + f"#{photo_id}")


def add_comment(request, photo_id):
    if request.method == "POST":
        photo = PetPhoto.objects.get(id=photo_id)
        form = PetPhotoCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()

    return redirect(request.META["HTTP_REFERER"] + f"#{photo_id}")
