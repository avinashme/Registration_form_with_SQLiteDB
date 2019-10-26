from django.db import models

GENDER_CHOICE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class RegistrationDetails(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE, default="")



