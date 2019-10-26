from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    url(r'^$', views.registration_form),
    url(r'^form_submission/$', views.form_submission),
    url(r'^form_submission/register_again/$', views.registration_form)

    # path('', views.registration_form),
    # path('jiji sas', views.form_submission)

]
