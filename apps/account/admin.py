# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'password',
        'last_login',
        'is_superuser',
        'uuid',
        'created',
        'updated',
        'email',
        'first_name',
        'last_name',
        'country',
        'organization',
        'phone',
        'is_staff',
        'is_active',
        'date_joined',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'created',
        'updated',
        'is_staff',
        'is_active',
        'date_joined',
    )
    raw_id_fields = ('groups', 'user_permissions')
