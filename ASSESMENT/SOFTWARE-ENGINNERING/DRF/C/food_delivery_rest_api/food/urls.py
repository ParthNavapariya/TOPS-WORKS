from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, MenuItemViewSet, OrderViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="category")
router.register("menuitems", MenuItemViewSet, basename="menuitem")
router.register("orders", OrderViewSet, basename="order")

urlpatterns = router.urls
