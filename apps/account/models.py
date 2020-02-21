from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phone_field import PhoneField
from apps.common.core import CoreModel,CoreManager,CoreQuerySet



class UserManager(CoreManager, BaseUserManager):
    def get_queryset(self):
        return CoreQuerySet(self.model, using=self._db)

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must gave an email address")

        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(PermissionsMixin, CoreModel, AbstractBaseUser):
    email = models.EmailField(verbose_name=_("Email"), unique=True)
    first_name = models.CharField(verbose_name=_("First name"), max_length=30, blank=True, null=True)
    last_name = models.CharField(verbose_name=_("Last name"), max_length=30, blank=True, null=True)
    country =models.CharField(verbose_name=_("country"),max_length=100,blank=True,null=True)
    organization =models.CharField(verbose_name=_("organization"),max_length=100,blank=True,null=True)
    phone=PhoneField(verbose_name=_("phone"),blank=True,null=True)
    is_staff = models.BooleanField(
        _("staff status"), default=False, help_text=_("Designates whether the user can log into this admin site.")
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )

    date_joined = models.DateTimeField(default=timezone.now)
    manager=UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ("first_name", "last_name")
