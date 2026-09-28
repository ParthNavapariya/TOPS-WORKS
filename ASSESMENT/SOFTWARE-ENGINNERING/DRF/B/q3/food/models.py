from django.db import models
class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self): return self.name
class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='menu_items')
    is_available=models.BooleanField(default=True)
    def __str__(self): return self.name
class Order(models.Model):
    class Status(models.TextChoices):
        PENDING='pending','Pending'
        CONFIRMED='confirmed','Confirmed'
        DELIVERED='delivered','Delivered'
    customer_name=models.CharField(max_length=100)
    item=models.CharField(max_length=100)
    quantity=models.IntegerField()
    status=models.CharField(max_length=20,choices=Status.choices,default=Status.PENDING)
    def __str__(self): return f'{self.customer_name} - {self.item}'
