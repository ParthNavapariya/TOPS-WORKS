from django.urls import include,path
from rest_framework.routers import DefaultRouter
from .views import CategoryListAPIView,MenuItemViewSet,OrderViewSet
router=DefaultRouter()
router.register(r'menu-items',MenuItemViewSet,basename='menu-item')
router.register(r'orders',OrderViewSet,basename='order')
urlpatterns=[path('api/categories/',CategoryListAPIView.as_view()),path('api/',include(router.urls))]
