from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from .models import Main

class MainForm(ModelForm):

    #fio_worker = forms.CharField(max_length=150,label='fio_work')
    # date = forms.DateField(label='Дата')
    # date_end_powerka = forms.DateField(label='Срок окончания поверки')

    class Meta:
        cl = 'form-control'
        model = Main
        fields = ( 'fio_worker','date','interval','city','adress','fio_client','name_type','num_gos_reestr','num_fabric','amp_filed',
        'place','pokazaniya','date_end_powerka','view_svidet','num_svidet_powerka','result_powerka','hot_water','qh','method','etalon','plomba','num_telephone'
        )
        widgets = {
            'fio_worker':forms.TextInput(attrs={'class':cl,'readonly':'true'}),
            'date':forms.TextInput(attrs={'class':cl}),
            'interval': forms.Select(attrs={'class': cl,'onchange':'getNewDate()'}),
            'date_end_powerka':forms.TextInput(attrs={'class':cl}),
            'city':forms.Select(attrs={'class':cl}),
            'adress':forms.TextInput(attrs={'class':cl}),
            'fio_client':forms.TextInput(attrs={'class':cl}),
            'amp_filed': forms.TextInput(attrs={'class': cl}),
            'view_svidet':forms.Select(attrs={'class':cl}),
            'name_type':forms.TextInput(attrs={'class':cl,'placeholder':'Наименование, тип СИ'}),
            'num_gos_reestr':forms.TextInput(attrs={'class':cl,'placeholder':'№ гос. реестра'}),
            'num_fabric':forms.TextInput(attrs={'class':cl}),
            'place':forms.Select(attrs={'class':cl}),
            'pokazaniya':forms.TextInput(attrs={'class':cl}),
            'num_svidet_powerka':forms.TextInput(attrs={'class':cl}),
            'qh':forms.NumberInput(attrs={'class':cl}),
            'method':forms.Select(attrs={'class':cl}),
            'etalon':forms.Select(attrs={'class':cl}),
            'plomba':forms.Select(attrs={'class':cl}),
            'hot_water':forms.Select(attrs={'class':cl}),
            'result_powerka':forms.Select(attrs={'class':cl}),
            'num_telephone': forms.TextInput(attrs={'class': cl}),


        }


class MobailForm(ModelForm):


    class Meta:
        cl = 'form-control'
        model = Main
        fields = ( 'date','name_type','num_fabric',
        'pokazaniya','date_end_powerka','hot_water' )
        widgets = {
            'date':forms.TextInput(attrs={'class':cl}),
            'date_end_powerka':forms.TextInput(attrs={'class':cl}),
            'name_type':forms.TextInput(attrs={'class':cl}),
            'num_fabric':forms.TextInput(attrs={'class':cl}),
            'pokazaniya':forms.TextInput(attrs={'class':cl}),
            'hot_water':forms.Select(attrs={'class':cl}),
        }

class UserForm(ModelForm):


    class Meta:
        cl = 'form-control'
        model = User
        fields = ( 'last_name', )
        widgets = {
            'last_name':forms.Select(attrs={'class':cl}),
        }