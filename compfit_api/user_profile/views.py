from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files import File
from api.models import User
from user_profile.models import WorkoutPlaylist
from user_profile.serializers import *
from api.serializers import UserSerializer
from compfit_api.storages import MediaStore

import base64
import json
import os


# Create your views here.
def create_saved_workouts_playlist(new_user):
    print('\n\n=== api/user_profile/create_saved_workouts_playlist Helper Function request ===\n\tCreating the new playlist')

    return "complete"


@api_view(['POST'])
def update_profile_picture(request):
    print('\n\n === api/user_profile/profile_picture/update POST request ===\n\tUpdating the user\'s profile picture')
    current_user_data = json.loads(request.body.decode("utf-8"))
    user = User.objects.get(id=current_user_data['id'])
    file_obj = request.FILES.get


    # Convert the image string into an actual image: String -> Bytes -> ImageFile
    image_string = current_user_data['profile_picture_data']
    image_data = base64.b64decode(image_string)
    file_name = str(user.id) + "_profile_picture.jpg"

    # Create the image file and save it to S3
    with open(file_name, 'wb+') as f:
        new_image = File(f)
        new_image.write(image_data)
        user.profile_picture = new_image
        user.save()


    # Remove the profile picture from our directory
    os.remove(file_name)
    print("Profile picture was successfully saved at: " + user.profile_picture.name + "\n\n")

    user_serializer = UserSerializer(instance=user)

    return Response(user_serializer.data)


@api_view(['GET'])
def get_user_profile_picture(request):

    
    return Response("sent the user's profile picture")




@api_view(['GET'])
def get_users_workout_playlists(request, id):
    print('\n\n === api/user_profile/workout_playlist/get GET request ===\n\tGetting the user\'s workout playlists')
    playlists = WorkoutPlaylist.objects.filter(owner_id=id)

    list = []
    for p in playlists:
        serializer = WorkoutPlaylistSerializer(instance=p)
        list.append(serializer.data)

    return Response(list)
