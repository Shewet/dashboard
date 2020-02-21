from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import OrganizationSerializer, OrgUsersSerializer, OrgGroupsSerializer, OrgGroupUsersSerializer, OrgProductsSerializer, OrgProductUsers
from .models import Organization, OrgUsers, OrgGroups, OrgGroupUsers,OrgProducts,OrgProductUsers
from rest_framework.decorators import action

# Create your views here.
class OrgViewSet(viewsets.ModelViewSet):
    queryset=Organization.objects.all()
    serializer_class= OrganizationSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
        

class OrgUsersViewSet(viewsets.ModelViewSet):
    queryset=OrgUsers.objects.all()
    serializer_class= OrgUsersSerializer


class OrgGroupsViewSet(viewsets.ModelViewSet):
    queryset=OrgGroups.objects.all()
    serializer_class= OrgGroupsSerializer

class OrgGroupUsersViewSet(viewsets.ModelViewSet):
    queryset=OrgGroupUsers.objects.all()
    serializer_class= OrgGroupUsersSerializer

class OrgProductsViewSet(viewsets.ModelViewSet):
    queryset=OrgProducts.objects.all()
    serializer_class= OrgProductsSerializer

class OrgProductUsersViewSet(viewsets.ModelViewSet):
    queryset=OrgProductUsers.objects.all()
    serializer_class= OrgProductUsers
