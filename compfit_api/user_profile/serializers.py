from rest_framework import serializers
from .models import *


class WorkoutPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlaylist
        fields = '__all__'



