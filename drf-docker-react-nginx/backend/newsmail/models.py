from django.db import models

# Create your models here.


class SettingsForRequest(models.Model):
    email = models.EmailField(verbose_name="Email", default=None)
    password = models.CharField(verbose_name="Пароль",max_length=20)


    

