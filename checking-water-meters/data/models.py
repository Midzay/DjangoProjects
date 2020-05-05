from django.db import models
from django.db.models import Count, Min, Sum, Avg
from django.contrib.auth import get_user_model


class Main(models.Model):
    YES_NO = ((1, 'ДА'), (0, 'НЕТ'))
    YES_NO_WATER = ((1, 'Горячая'), (0, 'Холодная'))
    fio_worker = models.CharField(max_length=300, db_index=True, verbose_name='ФИО работника')
    date = models.DateField(db_index=True, verbose_name='Дата')
    interval = models.ForeignKey('Interval', null=True, on_delete=models.PROTECT, verbose_name='МПИ')
    city = models.ForeignKey('City', null=True, on_delete=models.PROTECT, verbose_name='Город',db_index =True)
    adress = models.CharField(max_length=300, verbose_name='Адрес')
    fio_client = models.CharField(max_length=300, verbose_name='ФИО клиента')
    name_type = models.CharField(max_length=150, verbose_name='Наименование, тип СИ')
    num_gos_reestr = models.CharField(max_length=50, verbose_name='№ гос. реестра')
    num_fabric = models.CharField(max_length=150, verbose_name='Заводской номер',db_index =True)
    amp_filed = models.CharField(max_length=150, verbose_name='№ АМП', null=True, blank=True, default='-')
    place = models.ForeignKey('Place', null=True, on_delete=models.PROTECT, verbose_name='Место расположения счетчика')
    pokazaniya = models.CharField(max_length=125, verbose_name='Показания счетчика')
    date_end_powerka = models.DateField(verbose_name='Срок окончания поверки',db_index =True)
    view_svidet = models.ForeignKey('View_svidet', null=True, on_delete=models.PROTECT,
                                    verbose_name='Серия свидетельства', blank=True)
    num_svidet_powerka = models.CharField(max_length=125, verbose_name='№ св-ва о поверке',db_index =True)
    result_powerka = models.IntegerField(choices=YES_NO, verbose_name='Результат поверки(годен)')
    qh = models.FloatField(verbose_name='Qh')
    hot_water = models.IntegerField(choices=YES_NO_WATER, verbose_name='Вода',db_index =True)
    method = models.ForeignKey('Method', null=True, on_delete=models.PROTECT, verbose_name='Методика')
    etalon = models.ForeignKey('Etalon', null=True, on_delete=models.PROTECT, verbose_name='Используемый эталон')
    plomba = models.IntegerField(choices=YES_NO, verbose_name='Наличие пломбы')
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    num_telephone = models.CharField(max_length=300, blank=True, default=0, verbose_name='Номер телефона')

    class Meta:
        verbose_name_plural = "Поверки"
        verbose_name = 'Результат поверки'
        ordering = ['-date', '-published']


class City(models.Model):
    city = models.CharField(max_length=140, db_index=True, verbose_name='Город')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = "Города"
        verbose_name = 'Город'


class Place(models.Model):
    def __str__(self):
        return self.place

    place = models.CharField(max_length=140, db_index=True, verbose_name='Место расположения счетчика')

    class Meta:
        verbose_name_plural = "Места расположения счетчика"
        verbose_name = 'Место расположения'


class Method(models.Model):
    def __str__(self):
        return self.method

    method = models.CharField(max_length=140, db_index=True, verbose_name='Методика')

    class Meta:
        verbose_name_plural = "Методики"
        verbose_name = 'Методика'


class Etalon(models.Model):
    def __str__(self):
        return self.etalon

    etalon = models.CharField(max_length=140, db_index=True, verbose_name='Используемый эталон')
    full_name = models.CharField(max_length=240, default= '0', db_index=True, verbose_name='Полное наименование')

    class Meta:
        verbose_name_plural = "Эталоны"
        verbose_name = 'Эталон'


class View_svidet(models.Model):
    def __str__(self):
        return self.view_svidet

    view_svidet = models.CharField(max_length=40, db_index=True, verbose_name='Вид свидетельства')

    class Meta:
        verbose_name_plural = "Виды свидетельства"
        verbose_name = 'Вид свидетельства'


class DefaultForUser(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT,
                             verbose_name='Пользователь', unique=True)
    view_svidet = models.ForeignKey('View_svidet', null=True, on_delete=models.PROTECT,
                                    verbose_name='Серия свидетельства', blank=True)
    amp_boolean = models.BooleanField(verbose_name='Использовать номер антимагнитной пломбы', default=False)
    etalon = models.ForeignKey('Etalon', null=True, on_delete=models.PROTECT, verbose_name='Используемый эталон',
                               blank=True)
    protokol13 = models.CharField(max_length=140, null=True, blank=True, verbose_name='Протокол строка 13')
    protokol14 = models.CharField(max_length=140, null=True, blank=True, verbose_name='Протокол строка 14')
    protokol15 = models.CharField(max_length=140, null=True, blank=True, verbose_name='Протокол строка 15')
    name_for_protokol = models.CharField(max_length=140, null=True, blank=True, verbose_name='Подписная часть протокола')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Настройки по умолчанию для пользователя"
        verbose_name = 'Настройки по умолчанию для пользователя'


class Interval(models.Model):
    def __str__(self):
        return self.interval

    interval = models.CharField(max_length=140, db_index=True, verbose_name='Интервал поверки')

    class Meta:
        verbose_name_plural = "Интревал поверки"
        verbose_name = 'Интервал поверки'


class PreviouslyFormedProtocol(models.Model):

    fio_worker = models.CharField(max_length=140, null=True, blank=True, verbose_name='ФИО работника')
    view_svidet = models.CharField(max_length=140, null=True, blank=True, verbose_name='Вид свидетельства')
    range_number = models.CharField(max_length=140, null=True, blank=True, verbose_name='Диапазон')
    data_create  = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return str(self.data_create)

    class Meta:
        verbose_name_plural = "Автоматическое формирование протоколов"
        verbose_name = "Автоматическое формирование протоколов"