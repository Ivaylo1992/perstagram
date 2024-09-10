from django.urls import path, include
from petstagram3.accounts import views

urlpatterns = (
    path("register/", views.PetstagramUserRegisterView.as_view(), name="register"),
    path("login/", views.PetstagramUserLoginView.as_view(), name="login"),
    path("logout/", views.PetstagramUserLogoutView.as_view(next_page="index"), name="logout"),
    path("profile/<int:pk>/", include([
        path("", views.ProfileDetailsView.as_view(), name="profile_details"),
        path("edit/", views.PetstagramUserEditView.as_view(), name="profile_edit"),
        path("delete/", views.PetstagramUserDeleteView.as_view(), name="profile_delete"),
    ]))
)

# TODO: Create a profile delete link
