"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from apps.product import views as prod_view
from rest_framework import routers
from apps.organization.views import OrgViewSet, OrgUsersViewSet, OrgGroupUsersViewSet, OrgGroupsViewSet, OrgProductsViewSet, OrgProductUsersViewSet

orgrouter = routers.SimpleRouter()
orgrouter.register(r'api/organization', OrgViewSet,basename='Organization')

orgusersrouter = routers.SimpleRouter()
orgusersrouter.register(r'api/organization/users', OrgUsersViewSet,basename='OrgUsers')

orggrouprouter = routers.SimpleRouter()
orggrouprouter.register(r'api/organization/groups', OrgGroupsViewSet,basename='OrgGroups')

orggroupusersrouter = routers.SimpleRouter()
orggroupusersrouter.register(r'api/organization/group/users', OrgGroupUsersViewSet,basename='OrgGroupUsers')

orgproductrouter = routers.SimpleRouter()
orgproductrouter.register(r'api/organization/products', OrgProductsViewSet,basename='OrgProducts')

orgproductusersrouter = routers.SimpleRouter()
orgproductusersrouter.register(r'api/organization/product/users', OrgProductUsersViewSet,basename='OrgProductUsers')



router = routers.SimpleRouter()
router.register(r'api/product', prod_view.ProductViewSet,basename='Product')




urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'^api/', include('rest_framework.urls')),
] +router.urls 

urlpatterns += orgproductusersrouter.urls +orggroupusersrouter.urls + orgusersrouter.urls + orggrouprouter.urls +  orgproductrouter.urls  +orgrouter.urls
