from django.db import models
from .validators import name_validator, age_validator, advanced_name_validator, hours_per_day_validator, \
    device_validator


# Create your models here.


class SurveyData(models.Model):
    name = models.CharField(max_length=50, validators=[name_validator])
    surname = models.CharField(max_length=50, validators=[name_validator])
    age = models.IntegerField(validators=[age_validator])
    favorite_genre = models.CharField(max_length=70, validators=[name_validator])
    favorite_game = models.CharField(max_length=70, validators=[advanced_name_validator])
    number_of_hours = models.IntegerField()
    hours_per_day = models.IntegerField(validators=[hours_per_day_validator])
    first_experience = models.DateField()
    favorite_male_character = models.CharField(max_length=70, validators=[name_validator])
    favorite_female_character = models.CharField(max_length=70, validators=[name_validator])
    device = models.CharField(max_length=70,validators=[device_validator])

    def __str__(self):
        return f'{self.name} {self.surname}'
