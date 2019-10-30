from django.http import HttpResponse
from django.shortcuts import render
from .models import RegistrationDetails
# from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .custom_qr_code import qrcode_generator


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
    send_email_register_user(request)
    return render(request, 'form_submitted.html')


def send_email_register_user(request):
    firstn = request.POST.get('firstName', '')
    lastn = request.POST.get('lastName', '')
    to = request.POST.get('email', '')
    subject = 'You have successfully Registered!'
    msg = f'You are successfully registered Mr. {firstn} {lastn} please show below QR code at the Day of Event.'
    from_email = 'mesmarthackist@gmail.com'

    email = EmailMessage(subject, msg, from_email, [to])
    qrcode_generator.qr_code_generator(to)
    email.attach("QRCode/myqrcode1.svg", 'image/svg')
    email.send(fail_silently=False)


# def qr_code_generator(email):
#     url = pyqrcode.create(email)
#     path = os.path.join(os.getcwd(), "../RCode")
#     url.svg(f"{path}/app1.png", scale=8)
#     print('QR code successfully created')


# def send_email_register_user(request):
#     firstName = request.POST.get('firstName', '')
#     lastName = request.POST.get('lastName', '')
#     email = request.POST.get('email', '')
#     send_mail(
#         'You have successfully Registered!',
#         f'You are successfully registered Mr. {firstName} {lastName} please show below QR code at the Day of Event.',
#         'mesmarthackist4@gmail.com',
#         [email],
#         fail_silently=False
#     )
#     return HttpResponse(request,'Email Sent')
