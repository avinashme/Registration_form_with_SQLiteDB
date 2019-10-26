from django.http import HttpResponse
from django.shortcuts import render
from .models import RegistrationDetails


def registration_form(request):
    return render(request, 'index.html')


def form_submission(request):
    first_name = request.POST['firstName']
    last_name = request.POST['lastName']
    email = request.POST['email']
    mobile_number = request.POST['Number']
    gender = request.POST['gender']

    registration_details = RegistrationDetails(first_name=first_name, last_name=last_name, email=email,
                                               mobile_number=mobile_number, gender=gender)
    registration_details.save()
    return render(request, 'form_submitted.html')


def register_again(request):
    render(request, 'index.html')
