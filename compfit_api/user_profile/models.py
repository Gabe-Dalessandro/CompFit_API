from django.db import models


# Create your models here.
class WorkoutPlaylist(models.Model):
    # playlist_id = models.IntegerField(primary_key=True)
    playlist_name = models.CharField(max_length=50)
    date_created = models.DateField()

    # Foreign Keys
    owner_id = models.ForeignKey('api.User', on_delete=models.CASCADE, to_field='id', null=False, db_column='owner_id')

    class Meta:
        db_table = 'workout_playlist'
