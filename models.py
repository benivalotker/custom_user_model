from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
'''
See Django API for AbstractBaseUser & BaseUserManager required methods.
'''
class ProfileManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('must have an email address')
        if not username:
            raise ValueError('must have an user name')

        # create the user
        user = self.model(
            email=self.normalize_email(email),  # normalize_email - convert email to lower case (BaseUserManager function)
            username=username,                  
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),  # normalize_email - convert email to lower case (BaseUserManager function)
            password = password,
            username=username,                  
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Profile(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = ProfileManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

