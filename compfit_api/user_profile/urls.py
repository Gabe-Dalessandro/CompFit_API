from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from . import views


def api(request):
    print('\n\n === API Requested ===\n')
    return HttpResponse('using api/user_profile')


urlpatterns = [
    path('', api),
    path('profile_picture/update/', views.update_profile_picture),
    path('profile_picture/get/', views.get_user_profile_picture),
    path('workout_playlist/get/<str:id>/', views.get_users_workout_playlists)
]
