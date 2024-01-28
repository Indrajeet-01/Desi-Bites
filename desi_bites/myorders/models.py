from django.db import models
from menu.models import MenuItem

class UserOrder(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    items = models.ManyToManyField(MenuItem, through='UserOrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class UserOrderItem(models.Model):
    order = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
