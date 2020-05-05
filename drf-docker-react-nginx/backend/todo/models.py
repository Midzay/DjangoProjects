from django.db import models


# Create your models here.
class MatrixTodo(models.Model):
    title = models.CharField('Задача', max_length=1000)
    completed = models.BooleanField('Выполнено', default=False)
    class_task = models.IntegerField('Класс задачи')
    date_create = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['date_create']
