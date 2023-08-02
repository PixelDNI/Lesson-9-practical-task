from django.shortcuts import render
from .models import SurveyData
# Create your views here.


from django.core.exceptions import ValidationError
from .validators import name_validator, age_validator, hours_per_day_validator


def survey(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        genre = request.POST.get('genre')
        fgame = request.POST.get('fgame')
        number_of_hours = request.POST.get('number_of_hours')
        mcharacter = request.POST.get('m_character')
        fcharacter = request.POST.get('f_character')
        device = request.POST.get('device')
        first_experience = request.POST.get('first_experience')
        number_of_hours_per_day = request.POST.get('number_of_hours_per_day')

        try:
            name_validator(name)
        except ValidationError as e:
            return render(request, 'index.html', {'error_message': str(e)})

        try:
            name_validator(surname)
        except ValidationError as e:
            return render(request, 'index.html', {'error_message': str(e)})

        try:
            age_validator(age)
        except ValidationError as e:
            return render(request, 'index.html', {'error_message': str(e)})

        try:
            hours_per_day_validator(number_of_hours_per_day)
        except ValidationError as e:
            return render(request, 'index.html', {'error_message': str(e)})

        SurveyData.objects.create(
            name=name,
            surname=surname,
            age=age,
            favorite_genre=genre,
            favorite_game=fgame,
            number_of_hours=number_of_hours,
            hours_per_day=number_of_hours_per_day,
            first_experience=first_experience,
            favorite_male_character=mcharacter,
            favorite_female_character=fcharacter,
            device=device,
        )

    return render(request, 'index.html')


def plug(request):
    return render(request, 'plug.html')