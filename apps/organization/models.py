from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phone_field import PhoneField
from apps.common.core import CoreModel,CoreManager,CoreQuerySet
from apps.account.models import User
from apps.product.models import Product


# Create your models here.
class Organization(CoreModel):
    name=models.CharField(verbose_name=_("Name"), max_length=30, blank=True, null=True)
    slug=models.SlugField(verbose_name=_("Slug"),max_length = 240, null = True, blank = True) 
    address=models.TextField(verbose_name=_("Address"),null = True, blank = True)
    phone=PhoneField(verbose_name=_("phone"),blank=True,null=True)
    country=models.CharField(verbose_name=_("Country"),max_length=240,null=True,blank=True)
    date_joined= models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("name", "slug")
    
    def __str__(self):
        return self.name


class OrgUsers(CoreModel):
    uniqueno=models.CharField(verbose_name=_("Unique Number"),max_length=120,null=True,blank=True)
    first_name = models.CharField(verbose_name=_("First name"), max_length=30, blank=True, null=True)
    last_name = models.CharField(verbose_name=_("Last name"), max_length=30, blank=True, null=True)
    email=models.EmailField(verbose_name=_("Email"), unique=True)
    addedby=models.ForeignKey(User,related_name='+',on_delete=models.SET_NULL,blank=True, null=True)
    org=models.ForeignKey(Organization,related_name='+',on_delete=models.SET_NULL,blank=True, null=True)
    start_date=models.DateTimeField(verbose_name=_("Start Date"),default=timezone.now)
    end_date=models.DateTimeField(verbose_name=_("End Date"),blank=True,null=True)
    
    def __str__(self):
        return (self.org.name,self.user.firstname+" "+self.user.lastname)

class OrgGroups(CoreModel):
    org=models.ForeignKey(Organization,related_name='+',on_delete=models.SET_NULL,blank=True, null=True)
    name=models.CharField(verbose_name=_("Name"), max_length=30, blank=True, null=True)
    description=models.TextField(verbose_name=_("Description"),null = True, blank = True)
    addedby=models.ForeignKey(User,related_name='+',on_delete=models.SET_NULL,blank=True, null=True)

class OrgGroupUsers(CoreModel):
    org=models.ForeignKey(Organization,related_name='+',on_delete=models.SET_NULL,blank=True, null=True)
    group=models.ForeignKey(OrgGroups,related_name='+',on_delete=models.SET_NULL,blank=True, null=True)
    user=models.ForeignKey(OrgUsers,related_name='+',on_delete=models.SET_NULL,blank=True, null=True)
    start_date=models.DateTimeField(verbose_name=_("Start Date"),default=timezone.now)
    end_date=models.DateTimeField(verbose_name=_("End Date"),blank=True,null=True)

    def __str__(self):
        return (self.org.name,self.group.name,self.user.firstname+" "+self.user.lastname)


class OrgProducts(CoreModel):
    org=models.ForeignKey(Organization,related_name='+',on_delete=models.SET_NULL,blank=True, null=True)
    product=models.ForeignKey(Product,related_name='+',on_delete=models.SET_NULL,blank=True, null=True)
    licenses=models.IntegerField(verbose_name=_("Licenses"),default=10,blank=True,null=True)
    start_date=models.DateTimeField(verbose_name=_("Start Date"),default=timezone.now)
    end_date=models.DateTimeField(verbose_name=_("End Date"),blank=True,null=True)


class OrgProductUsers(CoreModel):
    org=models.ForeignKey(Organization,related_name='+',on_delete=models.SET_NULL,blank=True, null=True)
    product=models.ForeignKey(OrgProducts,related_name='+',on_delete=models.SET_NULL,blank=True, null=True)
    user=models.ForeignKey(OrgUsers,related_name='+',on_delete=models.SET_NULL,blank=True, null=True)
    addedby=models.ForeignKey(User,related_name='+',on_delete=models.SET_NULL,blank=True, null=True)
    start_date=models.DateTimeField(verbose_name=_("Start Date"),default=timezone.now)
    end_date=models.DateTimeField(verbose_name=_("End Date"),blank=True,null=True)

    def __str__(self):
        return (self.org.name,self.product.name,self.user.firstname+" "+self.user.lastname)

