# Generated by Django 3.0.2 on 2020-05-03 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MatrixTodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='Задача')),
                ('completed', models.BooleanField(default=False, verbose_name='Выполнено')),
                ('class_task', models.IntegerField(verbose_name='Класс задачи')),
                ('date_create', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ['date_create'],
            },
        ),
    ]