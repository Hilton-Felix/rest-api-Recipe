from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, password=None):
        
        if not email:
            raise ValueError('You did not provide an email address')
        
        if not first_name:
            raise ValueError('You did not provide your first name')

        if not last_name:
            raise ValueError('You did not provide your last name')

        user = self.model(
            email= self.normalize_email(email), 
            first_name=first_name, 
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
   

        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            password=password
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)





class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return f"{self.first_name}"