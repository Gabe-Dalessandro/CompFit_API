from django.db import models
from api.models import *


# Create your models here.
class WorkoutPlaylist(models.Model):
    # playlist_id = models.IntegerField(primary_key=True)
    playlist_name = models.CharField(max_length=50)
    date_created = models.DateField()

    # Foreign Keys
    owner = models.ForeignKey('api.User', on_delete=models.CASCADE, to_field='id', null=False, db_column='owner_id')

    class Meta:
        db_table = 'workout_playlist'

    def __str__(self):
        return_str = "Workout Playlist Object: " + str(self.pk) + "\n"
        user_email = (User.objects.get(pk=self.owner.id)).email
        return_str += "Playlist Name: " + self.playlist_name + "   Owned By: " + user_email + "\n"
        return return_str


class Workout(models.Model):
    # workout_id = models.IntegerField(primary_key=True)
    date_created = models.DateField()
    workout_title = models.CharField(max_length=100)
    workout_desc = models.CharField(max_length=1000)
    premium_workout = models.BooleanField()
    workout_picture = models.ImageField(null=True, blank=True, upload_to="workout_pictures")

    # Foreign Keys
    workout_creator = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id', null=False, db_column='workout_creator_id')
    workout_type = models.ForeignKey(WorkoutType, on_delete=models.CASCADE, to_field='id', db_column='workout_type_id')

    class Meta:
        db_table = 'workout'


class PlaylistWorkout(models.Model):
    # playlist_workout_id = models.IntegerField(primary_key=True)
    playlist = models.ForeignKey(WorkoutPlaylist, on_delete=models.CASCADE, to_field='id', db_column='playlist_id')
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, to_field='id', db_column='workout_id')
    date_created = models.DateField()

    class Meta:
        db_table = 'playlist_workout'

