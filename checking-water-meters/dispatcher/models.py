from django.db import models
from datetime import date

# Create your models here.
class Dispatcher(models.Model):
    YES_NO = ((1, 'ДА'), (0, 'НЕТ'))
    YES_NO_WATER = ((1, 'Горячая'), (0, 'Холодная'))
    date = models.DateField(verbose_name='Дата установки')
    fio_client = models.CharField(max_length=300, verbose_name='ФИО клиента')
    phone = models.CharField(max_length=50, verbose_name='Контактный телефон')
    adress = models.CharField(max_length=300, verbose_name='Адрес места эксплуатации (места установки)')
    name_type = models.CharField(max_length=150, verbose_name='Тип (наименование) модель, счетчика')
    num_fabric = models.CharField(max_length=150, verbose_name='Заводской номер')
    pokazaniya = models.CharField(max_length=125, verbose_name='Текущие показания')
    last_update = models.DateField(verbose_name='Последнее обновление показаний')
    hot_water = models.IntegerField(choices=YES_NO_WATER, verbose_name='Тип энергоресурса : вода Х/Г')
    num_dogovor = models.CharField(max_length=300, db_index=True, verbose_name='Договор №')

    class Meta:
        verbose_name_plural = "Показания"
        verbose_name = 'Результат '
        ordering = ['-date']

