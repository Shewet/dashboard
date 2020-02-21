from django.db import models
from django.utils.translation import gettext_lazy as _
import  apps.common
from apps.common.core import CoreModel


class Product(CoreModel):
    owned_by= models.CharField(verbose_name=_("Owner"),max_length=100,default=None)
    name= models.CharField(verbose_name=("Name"),max_length=100,unique=True)
    description= models.TextField(verbose_name="Description",blank=True,null=True)
    price=models.IntegerField(default=100)
    currency=models.CharField(max_length=30, default="INR")

    def __str__(self):
        return self.name


