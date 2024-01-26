from django.contrib import admin
from .models import UserAccount

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_active', 'is_staff')
    list_editable = ('is_active', 'is_staff')

admin.site.register(UserAccount, UserAdmin)

# Register your models here.
