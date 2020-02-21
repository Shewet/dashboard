from rest_framework import serializers
from .models import Organization, OrgUsers, OrgGroups, OrgGroupUsers, OrgProductUsers, OrgProducts
from apps.product.models import Product

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields= ( 'is_active', 'name', 'slug', 'address', 'phone', 'country', 'date_joined',)
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class OrgUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrgUsers
        fields= ( 'uuid', 'is_active', 'uniqueno', 'first_name', 'last_name', 'email', 'org', 'start_date', 'end_date',)

class OrgGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgGroups
        fields= ('uuid', 'is_active', 'org', 'name', 'description', )

class OrgGroupUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgGroupUsers
        fields=(
        'uuid', 'is_active', 'org', 'group', 'user', 'start_date', 'end_date', )
        
class OrgProductsSerializer(serializers.ModelSerializer):
    org_name=serializers.RelatedField(source='Organization.name', read_only=True)
    product_name=serializers.RelatedField(source='Product.name',read_only=True)

    class Meta:
        model =OrgProducts
        fields =(  
          'org_name', 'product_name', 'licenses', 'start_date', 'end_date','is_active',

        )

class OrgProductUsers(serializers.ModelSerializer):
    org=serializers.RelatedField(source='Organization', read_only=True)
    user=serializers.RelatedField(source='OrgUsers',read_only=True)
    product=serializers.RelatedField(source='Product',read_only=True)
    class Meta:
        model =OrgProductUsers
        fields =(
        'uuid', 'is_active', 'org', 'product', 'user', 'start_date', 'end_date', )