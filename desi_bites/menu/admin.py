from django.contrib import admin
from .models import MenuItem

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description','price')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'category')
    list_per_page = 25

admin.site.register(MenuItem, MenuAdmin)

# Register your models here.
