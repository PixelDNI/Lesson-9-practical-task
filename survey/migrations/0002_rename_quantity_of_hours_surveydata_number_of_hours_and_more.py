# Generated by Django 4.2.3 on 2023-07-29 05:07

from django.db import migrations, models
import survey.validators


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveydata',
            old_name='quantity_of_hours',
            new_name='number_of_hours',
        ),
        migrations.AlterField(
            model_name='surveydata',
            name='age',
            field=models.IntegerField(validators=[survey.validators.age_validator]),
        ),
        migrations.AlterField(
            model_name='surveydata',
            name='device',
            field=models.CharField(max_length=70, validators=[survey.validators.advanced_name_validator]),
        ),
        migrations.AlterField(
            model_name='surveydata',
            name='favorite_female_character',
            field=models.CharField(max_length=70, validators=[survey.validators.name_validator]),
        ),
        migrations.AlterField(
            model_name='surveydata',
            name='favorite_game',
            field=models.CharField(max_length=70, validators=[survey.validators.advanced_name_validator]),
        ),
        migrations.AlterField(
            model_name='surveydata',
            name='favorite_genre',
            field=models.CharField(max_length=70, validators=[survey.validators.name_validator]),
        ),
        migrations.AlterField(
            model_name='surveydata',
            name='favorite_male_character',
            field=models.CharField(max_length=70, validators=[survey.validators.name_validator]),
        ),
        migrations.AlterField(
            model_name='surveydata',
            name='hours_per_day',
            field=models.IntegerField(validators=[survey.validators.hours_per_day_validator]),
        ),
        migrations.AlterField(
            model_name='surveydata',
            name='name',
            field=models.CharField(max_length=50, validators=[survey.validators.name_validator]),
        ),
        migrations.AlterField(
            model_name='surveydata',
            name='surname',
            field=models.CharField(max_length=50, validators=[survey.validators.name_validator]),
        ),
    ]
