from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from . import views


def api_test_user(request):
    print('\n\n === API Requested ===\n')
    return HttpResponse('api test')


urlpatterns = [
    path('', api_test_user),
    path('register2/', views.register_new_user2),
    path('onboard/', views.onboard_user),
    path('register/', views.register_new_user),
    path('login/', views.user_login),
    path('get/<str:id>/', views.get_user_by_id),
    path('workout_type/get/', views.get_workout_types),
    path('search/get/<str:search_param>/', views.search_users)
    # path('user/<str:id>/', views.getUserById),
    # path('gender/get/', views.getGenderJson),
    # path('gender/get/<str:pk>/', views.getGenderJsonById),
    # path('gender/create/', views.genderCreate)
]
