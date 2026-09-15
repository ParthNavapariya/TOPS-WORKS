from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    pagination_class = LimitOffsetPagination

    filter_backends = [OrderingFilter, DjangoFilterBackend]

    ordering_fields = ['name', 'cuisine']

    filterset_fields = ['cuisine']