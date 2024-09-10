from django.urls import path, include
from petstagram3.common import views

urlpatterns = (
    path("", views.IndexView.as_view(), name="index"),
    path("like/<int:photo_id>/", views.like_functionality, name="like"),
    path("share/<int:photo_id>/", views.copy_link_to_clipboard, name="share"),
    path("comment/<int:photo_id>/", views.add_comment, name="comment"),
)