from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import  Dispatcher
#from .forms import MainForm
#from django.db.models import Q
from .functions import *

class SuperUserClass():

    def create_context(self, request):


        if request.method == 'GET':
            #q = Q(fio_worker=request.user.last_name)
            q=Q()
            main = Dispatcher.objects.filter(q)

            context = ClassPaginator().pagin(request, main)
            context['form'] = MainForm

            # agr = Dispatcher.objects.filter(q).aggregate(
            #     cnt=Count('date'), sum_p=Sum('result_powerka'))

        else:
            request.session['date_s'] = request.POST['date_s']
            request.session['date_po'] = request.POST['date_po']
            request.session['search_adr'] = request.POST['search_adr']
            request.session['view_svidet'] = request.POST['view_svidet']
            request.session['city'] = request.POST['city']
            request.session['water'] = request.POST['water']
            s = request.session['date_s']
            po = request.session['date_po']
            adr = request.session['search_adr']
            view_svidet = request.session['view_svidet']
            c = request.session['city']
            wat = request.session['water']
            q = create_request_to_bd(
                s=s, po=po, adr=adr, view_svidet=view_svidet)
            q = q & Q(fio_worker=request.user.last_name)
            if wat !='9':
                q = q & Q(hot_water=wat)
            if  c != '0':
                q = q & Q(city__city=c)
            main = Dispatcher.objects.filter(q)
            context = ClassPaginator().pagin(request, main)
            context['date_s'] = s
            context['date_po'] = po
            context['search_adr'] = adr
            context['view_svidet'] = view_svidet
            context['form'] = MainForm
            context['city'] = c
            context['water'] = wat
       # agr = Main.objects.filter(q).aggregate(
        #    cnt=Count('date'), sum_p=Sum('result_powerka'))
        # if agr['cnt'] > 0:
        #     context['all'] = agr['cnt']
        #     context['pow_ok'] = agr['sum_p']
        #     context['pow_no'] = agr['cnt'] - agr['sum_p']
        # print (context)
        return (request, 'dispatcher/superuser/index.html', context)
