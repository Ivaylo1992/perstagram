from django.urls import path, include
from petstagram3.photos import views


urlpatterns = (
    path("add/", views.PetPhotoCreateView.as_view(), name="create_photo") ,
    path("<int:pk>/", include([
        path("", views.PetPhotoDetailsView.as_view(), name="photo_details"),
        path("edit/", views.PetPhotoEditView.as_view(), name="edit_photo"),
        path("delete/", views.PetPhotoDeleteView.as_view(), name="delete_photo"),
    ])),
)