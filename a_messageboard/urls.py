from django.urls import path
from a_messageboard.views import messageboard_view

urlpatterns = [
    path('', messageboard_view, name='messageboard'),
]