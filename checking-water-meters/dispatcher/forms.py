from django.forms import ModelForm, Form
from django import forms
import datetime
from .models import Dispatcher

DATE_INPUT_FORMATS = ['%Y-%m-%d']
class DateInput(forms.DateInput):
    input_type = 'date'


class MainForm(ModelForm):
    # fio_worker = forms.CharField(max_length=150,label='fio_work')
    # date = forms.DateField(label='Дата')
    # date_end_powerka = forms.DateField(label='Срок окончания поверки')
    #date = forms.DateField(initial=datetime.date.today)


    class Meta:
        input_formats = DATE_INPUT_FORMATS
        cl = 'form-control'
        model = Dispatcher
        fields = ('date', 'fio_client', 'phone', 'adress', 'name_type', 'num_fabric',
                  'pokazaniya', 'last_update', 'hot_water', 'num_dogovor')
        widgets = {
            'date': forms.TextInput(attrs={'class':cl}),
            'fio_client': forms.TextInput(attrs={'class': cl}),
            'adress': forms.TextInput(attrs={'class': cl}),
            'phone': forms.TextInput(attrs={'class': cl}),
            'name_type': forms.TextInput(attrs={'class': cl}),
            'num_fabric': forms.TextInput(attrs={'class': cl}),
            'pokazaniya': forms.TextInput(attrs={'class': cl}),
            'last_update': forms.TextInput(attrs={'class':cl}),
            'hot_water': forms.Select(attrs={'class': cl}),
            'num_dogovor': forms.TextInput(attrs={'class': cl}),
        }
