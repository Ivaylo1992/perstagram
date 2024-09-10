from django.urls import path, include
from petstagram3.pets import views

urlpatterns = (
    path("add/", views.PetCreateView.as_view(), name="add_pet"),
    path("<str:username>/pet/<slug:pet_slug>",include([
        path("", views.PetDetailsView.as_view(), name="pet_details"),
        path("edit/", views.PetEditView.as_view(), name="edit_pet"),
        path("delete/", views.PetDeleteView.as_view() ,name="delete_pet"),
    ])),
)