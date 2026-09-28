from django.urls import path
from .views import CategoryListAPIView

urlpatterns = [
    path('api/categories/', CategoryListAPIView.as_view(), name='category-list'),
]