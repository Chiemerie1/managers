from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

# Create your models here.


#### custom user manager
class CustomUserManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, company_name, password):

        if not email:
            raise ValueError("Please provide a correctly formatted email address")

        user = self.model(
            email = self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            company_name=company_name,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, username, email, password, **other_fields):

        other_fields.get("is_active", True)
        other_fields.get("is_staff", True)
        other_fields.get("is_superuser", True)

        user = self.model(
            email = self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        return user


#### Custom user
class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    company_name = models.CharField(
        max_length=200,
        help_text="Input the name of your office or business of enterprise",
        unique=True
    )
    company_reg_no = models.CharField(max_length=100, verbose_name="company regostration number or number of incoporation")
    branches = models.IntegerField(verbose_name="Number of enterprise branches")
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "company_name"
    REQUIRED_FEILDS = ["first_name", "last_name", "email", "company_name", "company_reg_no", "branches"]

    object = CustomUserManager()

    def __str__(self):
        return self.company_name




