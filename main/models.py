from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone



class CUserManager(BaseUserManager):

    def create_user(self, enterprise_name, first_name, last_name, email, password=None):
        
        if not enterprise_name:
            raise ValueError("Users must specify enterprise name")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            enterprise_name=enterprise_name

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, enterprise_name, first_name, last_name, email, password=None):
        
        user = self.create_user(
            enterprise_name,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    enterprise_name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(verbose_name="Email address", unique=False)
    date = models.DateTimeField(default=timezone)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CUserManager()


    USERNAME_FIELD = "enterprise_name"
    REQUIRED_FIELDS = ["first_name", "last_name", "email"]

    def __str__(self):
        return self.enterprise_name


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


    


