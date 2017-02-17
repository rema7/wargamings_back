from django.contrib import admin
from django.db.models import Count

from .models import Player


class MyPlayerAdmin(admin.ModelAdmin):

    change_user_password_template = None

    list_display = ['name', 'rating', 'exp_avg', 'exp_total', 'days_total', 'is_hidden', 'created_at']

    ordering = ['name']


admin.site.register(Player, MyPlayerAdmin)
