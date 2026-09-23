from django.urls import path
from .views import send_email,send_sms,create_checkout,success,cancel,home,google_jwt,protected_api

urlpatterns  = [
    path("send-email/",send_email),
    path("send-sms/",send_sms),
    path("create_checkout/",create_checkout),
    path("success/",success),
    path("cancel/",cancel),
    path('', home),
    path("google-jwt/",google_jwt),
    path("protected/", protected_api),

]