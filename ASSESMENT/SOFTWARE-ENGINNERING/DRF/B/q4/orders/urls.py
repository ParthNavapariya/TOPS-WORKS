from django.urls import path
from .views import PlaceOrderAPIView

urlpatterns = [
    path("my-orders/", PlaceOrderAPIView.as_view(), name="my-orders"),
]
