from django.urls import path
from a_users.views import profile_view, profile_edit_view, profile_settings_view, profile_emailchange_view, profile_emailverify_view, profile_delete_view

urlpatterns = [
    path('', profile_view, name='profile'),
    path('edit/', profile_edit_view, name='profile_edit'),
    path('onboarding/', profile_edit_view, name='profile-onboarding'),
    path('settings/', profile_settings_view, name='profile_settings'),
    path('emailchange/', profile_emailchange_view, name='profile_emailchange'),
    path('emailverify/', profile_emailverify_view, name='profile_emailverify'),
    path('delete/', profile_delete_view, name='profile_delete'),
]