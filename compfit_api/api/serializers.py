from rest_framework import serializers
from .models import *
import json


class WorkoutTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutType
        fields = '__all__'


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'


class UserFitnessExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessExperience
        fields = '__all__'


class WorkoutIntensitySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutIntensity
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    first_name = serializers.CharField(allow_blank=True)
    last_name = serializers.CharField(allow_blank=True)
    workout_types = serializers.SerializerMethodField('convert_workout_types_to_str')

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # We get the workout_types as a many to many field that returns the ids.
    # This converts them into strings and replaces the workout_types field with this new array of strings
    def convert_workout_types_to_str(self, user):
        workout_type_query_set = UserWorkoutPreference.objects.filter(user=user.id)

        # if len(workout_type_query_set) != 0:
        #     print(workout_type_query_set[0].workout_type)

        workout_types = WorkoutType.objects.filter(user=user.id)
        workout_types_titles = []

        for wt in workout_types:
            workout_types_titles.append(wt.workout_type_title)
        return workout_types_titles


class UserWorkoutPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWorkoutPreference
        fields = '__all__'
