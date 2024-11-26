from django.urls import path
from users.views import profile_view, profile_edit_view, user_settings_view, user_view, user_password_change_view, user_delete_view, avatar_delete_view

urlpatterns = [
    path("", profile_view, name="profile"),
    path("edit/", profile_edit_view, name="profile_edit"),
    path("avatar_delete/", avatar_delete_view, name="avatar_delete"),
    path("onboarding/", profile_edit_view, name="profile_onboarding"),
    path("user/", user_view, name="user"),
    path("user_settings/", user_settings_view, name="user_settings"),
    path("user_password_change/", user_password_change_view, name="user_password_change"),
    path("user_delete/", user_delete_view, name="user_delete")
]