# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'created',
        'updated',
        'is_active',
        'owned_by',
        'name',
        'description',
    )
    list_filter = ('created', 'updated', 'is_active')
    search_fields = ('name',)
