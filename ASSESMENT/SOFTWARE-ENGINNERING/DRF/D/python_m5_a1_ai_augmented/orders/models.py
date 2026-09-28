from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    item = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"
