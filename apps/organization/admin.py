# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Organization, OrgUsers, OrgGroups, OrgGroupUsers, OrgProducts, OrgProductUsers


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'created',
        'updated',
        'is_active',
        'name',
        'slug',
        'address',
        'phone',
        'country',
        'date_joined',
    )
    list_filter = ('created', 'updated', 'is_active', 'date_joined')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}


@admin.register(OrgUsers)
class OrgUsersAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'created',
        'updated',
        'is_active',
        'uniqueno',
        'first_name',
        'last_name',
        'email',
        'addedby',
        'org',
        'start_date',
        'end_date',
    )
    list_filter = (
        'created',
        'updated',
        'is_active',
        'addedby',
        'org',
        'start_date',
        'end_date',
    )


@admin.register(OrgGroups)
class OrgGroupsAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'created',
        'updated',
        'is_active',
        'org',
        'name',
        'description',
        'addedby',
    )
    list_filter = ('created', 'updated', 'is_active', 'org', 'addedby')
    search_fields = ('name',)


@admin.register(OrgGroupUsers)
class OrgGroupUsersAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'created',
        'updated',
        'is_active',
        'org',
        'group',
        'user',
        'start_date',
        'end_date',
    )
    list_filter = (
        'created',
        'updated',
        'is_active',
        'org',
        'group',
        'user',
        'start_date',
        'end_date',
    )


@admin.register(OrgProducts)
class OrgProductsAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'created',
        'updated',
        'is_active',
        'org',
        'product',
        'licenses',
        'start_date',
        'end_date',
    )
    list_filter = (
        'created',
        'updated',
        'is_active',
        'org',
        'product',
        'start_date',
        'end_date',
    )


@admin.register(OrgProductUsers)
class OrgProductUsersAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'created',
        'updated',
        'is_active',
        'org',
        'product',
        'user',
        'addedby',
        'start_date',
        'end_date',
    )
    list_filter = (
        'created',
        'updated',
        'is_active',
        'org',
        'product',
        'user',
        'addedby',
        'start_date',
        'end_date',
    )
