from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .models import Category,MenuItem,Order
from .serializers import CategorySerializer,MenuItemSerializer,OrderSerializer

class CategoryListAPIView(ListAPIView):
    queryset=Category.objects.all(); 
    serializer_class=CategorySerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    
    queryset=MenuItem.objects.all(); 
    serializer_class=MenuItemSerializer
    
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class=OrderSerializer
    def get_queryset(self):
        queryset=Order.objects.all()
        status=self.request.query_params.get('status')
        if status: queryset=queryset.filter(status=status)
        return queryset
