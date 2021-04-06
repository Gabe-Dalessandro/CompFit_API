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
        # Password is incorrect
        else:
            print("password is incorrect")
            return Response("Password was Incorrect")
    # email does not exist
    else:
        print("email does not exist")
        return Response("Email does not exist")




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




@api_view(['POST'])
def register_new_user2(request):
    print('\n\n=== api/user/register POST request ===\n\tRegistering a new user')

    # Convert to usable json object
    new_user_json = json.loads(request.body.decode("utf-8"))
    # username = new_user_json["username"]
    email = new_user_json["email"]
    password = new_user_json["password"]

    # Check if username already exists
    # user_query_set = User.objects.filter(username=username)
    # if len(user_query_set) == 1:
    #     print("Error: Username already exists")
    #     return Response("Username is already being used by another account.")

    # Check if email already exists
    user_query_set = User.objects.filter(email=email)
    if len(user_query_set) == 1:
        print("Error: Email already exists")
        return Response("Email is already being used by another account.")

    # Create the new user and return the new user data
    new_user = User.objects.create(email=email, password=password)
    user_serializer = UserSerializer(instance=new_user)

    print("Successfully registered a new user!")
    return Response(user_serializer.data)


@api_view(['POST'])
def onboard_user(request):
    print('\n\n=== api/user/onboard POST request ===\n\tOnboarding the user')

    # Convert to usable json object
    user_json = json.loads(request.body.decode("utf-8"))

    # Get the existing user
    id = user_json["id"]
    updated_user = User.objects.filter(id=id)[0]

    # Update the user's data
    updated_user.email = user_json['email']
    updated_user.password = user_json['password']
    updated_user.phone_number = user_json['phone_number']
    updated_user.birthday = user_json['birthday']
    updated_user.total_points = user_json['total_points']
    updated_user.gender_desc = Gender.objects.filter(gender_desc=user_json['gender_desc'])[0]
    updated_user.fitness_exp_title = FitnessExperience.objects.filter(fitness_exp_title=user_json['fitness_exp_title'])[0]
    updated_user.workout_intensity_title = WorkoutIntensity.objects.filter(workout_intensity_title=user_json['workout_intensity_title'])[0]

    # Add workout types into UserWorkoutPreference Table (many to many table)
    workout_types = user_json['workout_types']
    for wt in workout_types:
        obj = WorkoutType.objects.filter(workout_type_title=wt)
        workout_type_obj = obj[0]
        UserWorkoutPreference.objects.create(user=updated_user, workout_type=workout_type_obj)

    # Save the user
    updated_user.save()

    # Create a "Saved Workouts" Playlist every time a new user is created
    create_saved_workouts_playlist(updated_user)
    #
    user_serializer = UserSerializer(instance=updated_user)
    print(user_serializer.data)
    return Response(user_serializer.data)


def create_saved_workouts_playlist(new_user):
    playlist_name = "Saved Workouts"
    date_created = datetime.now()

    WorkoutPlaylist.objects.create(owner=new_user, playlist_name=playlist_name, date_created=date_created)




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


@api_view(['GET'])
def search_users(request, search_param):
    print('\n\n === api/user/search/get/ GET request ===\n\tSearching for users with parameter: ' + search_param)
    user_query_set = User.objects.filter(email__icontains=search_param)

    # for user in user_query_set:
    #     print(user.email)

    users_json = []
    for user in user_query_set:
        user_serializer = UserSerializer(instance=user)
        users_json.append(user_serializer.data)

    return Response(users_json)
