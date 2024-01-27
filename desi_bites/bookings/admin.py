from django.contrib import admin
from .models import Reservation

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'date', 'guests')
    list_display_links = ('id','name')
    search_fields = ('id','name')
    list_per_page = 25

admin.site.register(Reservation, BookingAdmin)

# Register your models here.
