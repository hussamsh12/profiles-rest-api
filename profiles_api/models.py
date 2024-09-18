from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manages our UserProfile model"""

    def create_user(self, email, name, password=None):
        """Creates a user for the UserProfile"""

        if not email:
            raise ValueError("Must provide an email")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name) #Creates a user with the provided email and name

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates a superuser"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user



# Template for our UserProfile Table
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """A model for our UserProfile"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        """String Representation of our UserProfile"""
        return "Email = {}, Name = {}".format(self.email, self.name)