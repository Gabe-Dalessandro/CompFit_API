from django.db import models


# Create your models here.

class WorkoutType(models.Model):
    # workout_type_id = models.IntegerField(primary_key = true)
    workout_type_title = models.CharField(max_length=50, unique=True)
    class Meta:
        db_table = 'workout_type'

    def __str__(self):
        return_str = "Workout Type: id=" + str(self.id) + "  title=" + str(self.workout_type_title)
        return return_str


class Gender(models.Model):
    # gender_id = models.IntegerField(primary_key=True)
    gender_desc = models.CharField(max_length=30, unique=True)
    class Meta:
        db_table = 'gender'

    def __str__(self):
        return_str = "Gender: id=" + str(self.id) + "  desc=" + str(self.gender_desc)
        return return_str


class FitnessExperience(models.Model):
    # fitness_exp_id = models.IntegerField(primary_key=True)
    fitness_exp_title = models.CharField(max_length=20, unique=True)
    fitness_exp_desc = models.CharField(max_length=160, unique=True)
    class Meta:
        db_table = 'fitness_experience'

    def __str__(self):
        return_str = "Fitness Experience: id=" + str(self.id) + "  title=" + str(self.fitness_exp_title)
        return return_str


class WorkoutIntensity(models.Model):
    # workout_intensity_id = models.IntegerField(primary_key=True)
    workout_intensity_title = models.CharField(max_length=30, unique=True)
    workout_intensity_desc = models.CharField(max_length=160, unique=True)
    class Meta:
        db_table = 'workout_intensity'

    def __str__(self):
        return_str = "Workout Intensity: id=" + str(self.id) + "  title=" + str(self.workout_intensity_title)
        return return_str


class User(models.Model):
    # user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=10, null=True)
    birthday = models.DateField(null=True)
    total_points = models.IntegerField(null=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="profile_pictures")
    # user_description = models.TextField(blank=True, null=True)

    # Foreign Keys
    gender_desc = models.ForeignKey(Gender, on_delete=models.SET_NULL, to_field='gender_desc', null=True, db_column='gender_desc')
    fitness_exp_title = models.ForeignKey(FitnessExperience, on_delete=models.SET_NULL, null=True, to_field='fitness_exp_title', db_column='fitness_exp_title')
    workout_intensity_title = models.ForeignKey(WorkoutIntensity, on_delete=models.SET_NULL, null=True, to_field='workout_intensity_title', db_column='workout_intensity_title')
    workout_types = models.ManyToManyField(WorkoutType, through='UserWorkoutPreference')
    # level_number = models.ForeignKey('Levels', models.DO_NOTHING, db_column='level_number', null=True)
    class Meta:
        db_table = 'user'

    # @property
    # def age(self):
    #     return


class UserWorkoutPreference(models.Model):
    # user_workout_preference_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id', db_column='user_id')
    workout_type = models.ForeignKey(WorkoutType, on_delete=models.CASCADE, to_field='workout_type_title', db_column='workout_type')

    class Meta:
        db_table = 'user_workout_preference'

    def __str__(self):
        return_str = "User Workout Preference(MtoM): User(id=" + str(self.user.id) + " email=" + str(self.user.email)+")"\
                    + "  Workout Type(id=" + str(self.workout_type.id) + " title=" + str(self.workout_type.workout_type_title) + ")"
        return return_str



# To Delete all data in the database
# DELETE FROM workout_playlist *;
# DELETE FROM user_workout_preference *;
# DELETE FROM public.user *;
