# Generated by Django 2.2.3 on 2020-04-18 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_auto_20191116_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviouslyFormedProtocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio_worker', models.CharField(blank=True, max_length=140, null=True, verbose_name='ФИО работника')),
                ('view_svidet', models.CharField(blank=True, max_length=140, null=True, verbose_name='Вид свидетельства')),
                ('range_number', models.CharField(blank=True, max_length=140, null=True, verbose_name='Диапазон')),
                ('data_create', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'verbose_name': 'Автоматическое формирование протоколов',
                'verbose_name_plural': 'Автоматическое формирование протоколов',
            },
        ),
        migrations.AlterField(
            model_name='main',
            name='date_end_powerka',
            field=models.DateField(db_index=True, verbose_name='Срок окончания поверки'),
        ),
        migrations.AlterField(
            model_name='main',
            name='hot_water',
            field=models.IntegerField(choices=[(1, 'Горячая'), (0, 'Холодная')], db_index=True, verbose_name='Вода'),
        ),
        migrations.AlterField(
            model_name='main',
            name='num_fabric',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Заводской номер'),
        ),
        migrations.AlterField(
            model_name='main',
            name='num_svidet_powerka',
            field=models.CharField(db_index=True, max_length=125, verbose_name='№ св-ва о поверке'),
        ),
    ]
