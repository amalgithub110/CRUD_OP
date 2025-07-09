from django.contrib import admin
from .models import add_money

# Register your models here.

@admin.register(add_money)
class UserAdmin(admin.ModelAdmin):
    list_display=('for_what','how_much')