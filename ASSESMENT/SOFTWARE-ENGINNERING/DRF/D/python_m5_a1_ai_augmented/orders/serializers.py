from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "customer_name", "item", "quantity", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate_customer_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Customer name cannot be empty.")
        return value

    def validate_item(self, value):
        if not value.strip():
            raise serializers.ValidationError("Item cannot be empty.")
        return value

    def validate_quantity(self, value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise serializers.ValidationError("Quantity must be a positive integer.")
        if value <= 0:
            raise serializers.ValidationError("Quantity must be a positive integer.")
        return value
