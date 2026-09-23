from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.conf import settings 
import requests
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import stripe
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail

# Create your views here.

@api_view(["POST"])
def send_email(request):
    email = request.data.get('email')
    if not email :
        return Response({
            "error":"email is required"
        },status=400)
    send_mail(
        subject='welcome!',
        message='welcome to our application',
        from_email = None,
        recipient_list=[email],
    )
    return Response({
        "message":"welcome email sent successfully"
    })

@api_view(['POST'])
def send_sms(request):
    phone = request.data.get('phone')
    message_text = request.data.get('message')

    if not phone:
        return Response({
            "error": "phone is required"
        }, status=400)

    if not message_text:
        return Response({
            "error": "message is required"
        }, status=400)
    print(settings.ACCOUNT_SID,settings.AUTH_TOKEN)
    client = Client(
        settings.ACCOUNT_SID,
        settings.AUTH_TOKEN
    )

    message = client.messages.create(
        body="message_text",
        from_="+17372508034",
        to="+919574155158"
    )

    return Response({
        "message_sid": message.sid,
        "status": "sms sent successfully"
    })

stripe.api_key = settings.SECRET_KEY
@api_view(['POST'])
def create_checkout(request):
        amount = request.data.get('amount')
        currency= request.data.get("currency")
        if not amount:
            return Response({
                "error":"amount is required"
            },status = 400)
        if not currency:
            return Response({
                "error":"currency is required"
            },status=400)
        checkout_session = stripe.checkout.Session.create(
         payment_method_types=['card'],

         line_items=[{
             'price_data': {
                 'currency': currency,
                 'product_data': {
                     'name': 'Python Course'
                 },
                 'unit_amount': int(amount),
             },
             'quantity': 1,
         }],

         mode='payment',

         success_url='http://localhost:8000/api/success/',
         cancel_url='http://localhost:8000/api/cancel/',
     )

        return Response({
        "payment_status": "pending",
        "transaction_id": checkout_session.id,
        "checkout_url": checkout_session.url
    })

def success(request):
    return HttpResponse("payment done successfull")

def cancel(request):
    return HttpResponse("payment cancelled")


def home(request):
    return HttpResponse("Google Login Successful")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def google_jwt(request):
    refresh = RefreshToken.for_user(request.user)
    return Response({
        "user":request.user.username,
        "refresh":str(refresh),
        "access":str(refresh.access_token)
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_api(request):
    return Response({
        "message": "JWT token valid che",
        "user": request.user.username
    })