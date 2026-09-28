from django.urls import path
from .views import (
    CategoryListAPIView,
    MenuItemListCreateAPIView,
    MenuItemDetailAPIView,
)

urlpatterns = [
    path('api/categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('api/menu-items/', MenuItemListCreateAPIView.as_view(), name='menu-item-list-create'),
    path('api/menu-items/<int:pk>/', MenuItemDetailAPIView.as_view(), name='menu-item-detail'),
]
