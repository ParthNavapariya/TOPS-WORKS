from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializer

class PlaceOrderAPIView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {"success": False, "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        order = serializer.save()

        return Response(
            {
                "success": True,
                "message": "Order placed successfully.",
                "order": OrderSerializer(order).data,
            },
            status=status.HTTP_201_CREATED,
        )
