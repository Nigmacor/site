from django.db import models
from django.contrib.auth.models import AbstractUser

class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(default=True,
                    verbose_name='Слать оповещения о новых комментариях?')




"""
username - логин
password - пароль в закодированном виде. Обязательно к заполнению;
email - почта
first _ name - имя
last _ name - фамилия
is_active - True, если онлайн
is_staff - True, если персонал
is_superuser - True, если админ
last_login - дата и время последнего входа на сайт
is_authenticated - возвращает True, если пользователь выполнил вход
is_anonymous - как is_authenticated, но наоборот

Если что, к ним нужно привязать шаблон
"""
