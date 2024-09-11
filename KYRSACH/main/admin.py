from django.contrib import admin
from .models import CustomUser, UserProfile, Address, Wishlist, OrderHistory
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(Wishlist)
admin.site.register(OrderHistory)
