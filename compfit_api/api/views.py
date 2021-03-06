from django.http import JsonResponse
from django.http import HttpResponse

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import *
from user_profile.models import WorkoutPlaylist
import json
from datetime import date, datetime


# Create your views here.
@api_view(['GET'])
def get_user_by_id(request, id):
    print('\n\n=== User GET BY ID Requested ===\n\t Getting User by Id')
    user = User.objects.get(user_id=id)
    print(user)
    return HttpResponse('User GET BY ID called')


@api_view(['POST'])
def user_login(request):
    print('\n\n=== api/user/login GET request ===\n\tLogging user in')

    # Convert to a usable json object
    login_json = json.loads(request.body.decode("utf-8"))
    print(login_json)
    email = login_json['email']
    password = login_json['password']

    # check if email exists
    user_query_set = User.objects.filter(email=email)
    if len(user_query_set) != 0:
        # check if the password matches
        if user_query_set[0].password == password:
            logged_in_user = User.objects.get(email=email)
            serializer = UserSerializer(instance=logged_in_user)
            return Response(serializer.data)
        else:
            print("password is incorrect")
    else:
        print("email does not exist")
        return Response("user login")




# Register New User: This creates a new user and saves them into the database. It also creates a new
# "Saved Workouts" playlist whenever a new user is created
@csrf_exempt
@api_view(['POST'])
def register_new_user(request):
    print('\n\n=== api/user/register POST request ===\n\tRegistering a new user')

    # Convert to usable json object
    new_user_json = json.loads(request.body.decode("utf-8"))
    print(new_user_json)
    email = new_user_json['email']
    password = new_user_json['password']
    workout_types = new_user_json['workout_types']

    # Create the new user and have that data returned
    new_user = User.objects.create(email=email, password=password)

    # Add workout types into UserWorkoutPreference Table (many to many table)
    for wt in workout_types:
        obj = WorkoutType.objects.filter(workout_type_title=wt)
        workout_type_obj = obj[0]
        workoutPreference = UserWorkoutPreference.objects.create(user=new_user, workout_type=workout_type_obj)

    # add rest of attributes to the new user
    new_user.phone_number = new_user_json['phone_number']
    new_user.birthday = new_user_json['birthday']
    new_user.total_points = new_user_json['total_points']
    new_user.gender_desc = Gender.objects.filter(gender_desc=new_user_json['gender_desc'])[0]
    new_user.fitness_exp_title = FitnessExperience.objects.filter(fitness_exp_title=new_user_json['fitness_exp_title'])[0]
    new_user.workout_intensity_title = WorkoutIntensity.objects.filter(workout_intensity_title=new_user_json['workout_intensity_title'])[0]
    new_user.save()
    # Calculate the age
    # birthDate = datetime.strptime(newUser.birthday, '%Y-%m-%d')
    # today = date.today()
    # age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    # print(age)

    # Create a "Saved Workouts" Playlist every time a new user is created
    create_saved_workouts_playlist(new_user)

    serializer = UserSerializer(instance=new_user)
    print(serializer.data)
    return Response(serializer.data)


def create_saved_workouts_playlist(new_user):
    playlist_name = "Saved Workouts"
    date_created = datetime.now()

    WorkoutPlaylist.objects.create(owner_id=new_user, playlist_name=playlist_name, date_created=date_created)



# === Workout_Type Functions ===
@api_view(['GET'])
def get_workout_types(request):
    print('\n\n === api/workout_type/get GET request ===\n\tGetting All Workout_Types')
    workout_type_objs = WorkoutType.objects.all()

    workout_type_array = []

    for wt in workout_type_objs:
        workout_type_array.append(wt.workout_type_title)

    # print(workout_type_array)

    return Response(workout_type_array)


