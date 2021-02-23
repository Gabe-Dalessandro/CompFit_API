from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from . import views


def api(request):
    print('\n\n === API Requested ===\n')
    return HttpResponse('api test')


urlpatterns = [
    path('', api),
    path('register/', views.register_new_user),
    path('login/', views.user_login),
    path('get/<str:id>/', views.get_user_by_id),
    path('workout_type/get/', views.get_workout_types)
    # path('user/<str:id>/', views.getUserById),
    # path('gender/get/', views.getGenderJson),
    # path('gender/get/<str:pk>/', views.getGenderJsonById),
    # path('gender/create/', views.genderCreate)
]
