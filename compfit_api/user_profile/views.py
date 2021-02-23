from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files import File
from api.models import User
from api.serializers import UserSerializer

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

    # Convert the image string into an actual image: String -> Bytes -> ImageFile
    image_string = current_user_data['profile_picture']
    image_data = base64.b64decode(image_string)
    file_name = str(user.id) + "_profile_picture.jpg"
    f = open(file_name, 'wb+')
    new_image = File(f)
    new_image.write(image_data)

    # Remove the old profile picture if its in the directory and from the current directory
    cwd = os.getcwd()
    path = os.path.join(cwd, "media/profile_pictures/" + file_name)
    if os.path.exists(path):
        os.remove(user.profile_picture.path)
        print("Old profile picture was removed")

    # Set the new profile picture
    user.profile_picture = new_image
    os.remove(file_name)

    # Save the profile picture
    user.save()
    print("Profile picture was successfully saved at: \n\t" + user.profile_picture.path + "\n\n")

    return Response(user.profile_picture.path)



def get_user_profile_picture(request):

    return Response("sent the user's profile picture")
