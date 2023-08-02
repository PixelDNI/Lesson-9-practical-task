from django.core.exceptions import ValidationError
import string


def name_validator(value):
    alphabet = list(string.ascii_letters)
    for i in value:
        if i not in alphabet:
            raise ValidationError(f"{value} is not a valid name")

def age_validator(value):
    value = str(value)
    if not value.isdigit():
        raise ValidationError('Please enter a valid age')
    age = int(value)
    if age > 120 or age < 0:
        raise ValidationError('Please enter a valid age')

def advanced_name_validator(value):
    symbols = str(string.ascii_letters) + '1234567890&'
    for i in value:
        if i not in symbols:
            raise ValidationError(f"{value} is not a valid name")

def device_validator(value:str):
    devices = ['mobile phone', 'phone', 'gamepad', 'game console', 'computer', 'laptop', 'tablet', 'stone and stick']

    if value.lower() not in devices:
        return ValidationError(f"Input the field correctly !!! ")


def hours_per_day_validator(value):
    value = int(value)
    if value > 24 or value < 0:
        raise ValidationError('Please enter a number between 0 and 24')