from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from . import views


def api(request):
    print('\n\n === API Requested ===\n')
    return HttpResponse('using api/user_profile')


urlpatterns = [
    path('', api),
    # path('create_saved_workouts_playlist', views.create_saved_workouts_playlist),
    # path('user/login/', views.user_login),
    # path('user/get/<str:id>/', views.get_user_by_id),
    # path('workout_type/get/', views.get_workout_types)
]
