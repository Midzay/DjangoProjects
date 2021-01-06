# Generated by Django 2.2 on 2019-05-09 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20190506_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='View_svidet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_svidet', models.CharField(db_index=True, max_length=40, verbose_name='Вид свидетельства')),
            ],
            options={
                'verbose_name': 'Вид свидетельства',
                'verbose_name_plural': 'Виды свидетельства',
            },
        ),
        migrations.AddField(
            model_name='main',
            name='view_svidet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='data.View_svidet', verbose_name='Вид свидетельства'),
        ),
    ]