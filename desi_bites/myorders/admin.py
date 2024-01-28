from django.contrib import admin
from .models import UserOrder, UserOrderItem

class OrderItemInline(admin.TabularInline):
    model = UserOrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['full_name', 'phone', 'address', 'total_amount', 'created_at']
    search_fields = ['full_name', 'phone', 'address']

admin.site.register(UserOrder, OrderAdmin)

