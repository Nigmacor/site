from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from django.conf import settings

class CustomUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    is_active = models.BooleanField(default=False)
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/', blank=True)
    family = models.CharField(max_length=150, verbose_name='family', default=None)
    name = models.CharField(max_length=30, verbose_name='name', default=None)
    patronymic = models.CharField(blank=True, max_length=150, verbose_name='family')
    def __str__(self):
        return f'{self.first_name} {self.last_name}'.title()

'''
class CheckEmail(models.Model):
    random_string = '''
