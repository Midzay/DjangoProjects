from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Main, City, View_svidet
from .forms import UserForm
from django.contrib.auth.models import User
# from django.db.models import Q
from .functions import *
from django.db.models.functions import TruncMonth
import datetime


class UserClass():
    dict_month = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
                  9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}

    def create_context(self, request):
        today = datetime.datetime.now()

        if request.method == 'GET':

            q = Q(fio_worker=request.user.last_name)
            main = Main.objects.filter(q)
            context = ClassPaginator().pagin(request, main)

            q1 = Q(fio_worker=request.user.last_name) & Q(published__month=today.month) & Q(published__year=today.year)
            count_by_day_all = Main.objects.filter(q1).filter(date__month=today.month, date__year=today.year) \
                .values('date').annotate(my_count_date=Count('date')).annotate(
                result_powerka=Sum('result_powerka')).order_by(('-date'))
            context['curMon'] = today.month
            request.session['month'] = today.month
            context = PaginatorMobile().pagin(request, count_by_day_all, context)
            context['month_from_dict'] = self.dict_month[context['curMon']]

        else:

            if 'next' in request.POST:
                curMon = int(request.POST['curMon']) + 1
                if curMon > 12: curMon = 1
                request.session['month'] = curMon
                context = nextPredforMobile(request, curMon, today, self.dict_month)
                return (request, 'simpleuser/index.html', context)
            if 'pred' in request.POST:
                curMon = int(request.POST['curMon']) - 1
                if curMon < 1: curMon = 12
                request.session['month'] = curMon
                context = nextPredforMobile(request, curMon, today, self.dict_month)
                return (request, 'simpleuser/index.html', context)

            if 'back' in request.POST:
                curMon = request.session['month']
                context = nextPredforMobile(request, curMon, today, self.dict_month)
                return (request, 'simpleuser/index.html', context)

            if 'find_mobile' in request.POST:
                request.session['date'] = request.POST['date']
                request.session['num_svidet_powerka'] = request.POST['num_svidet_powerka']
                request.session['num_fabric'] = request.POST['num_fabric']
                q = createRequestMobile(date=request.session['date'],
                                        nsp=request.session['num_svidet_powerka'],
                                        nf=request.session['num_fabric']) & Q(fio_worker=request.user.last_name)

                return findRowsForMobile(request, q)

            request.session['date_s'] = request.POST['date_s']
            request.session['date_po'] = request.POST['date_po']
            request.session['search_adr'] = request.POST['search_adr']
            request.session['num_fabric'] = request.POST['num_fabric']
            request.session['num_svidet_powerka'] = request.POST['num_svidet_powerka']
            s = request.session['date_s']
            po = request.session['date_po']
            adr = request.session['search_adr']
            num_fabric = request.session['num_fabric']
            num_svidet_powerka = request.session['num_svidet_powerka']
            q = create_request_to_bd(s=s, po=po, adr=adr, num_fabric=num_fabric, n_s_v=num_svidet_powerka)
            q = q & Q(fio_worker=request.user.last_name)
            main = Main.objects.filter(q)
            context = ClassPaginator().pagin(request, main)
            context['date_s'] = s
            context['date_po'] = po
            context['search_adr'] = adr
        agr = Main.objects.filter(q).aggregate(
            cnt=Count('date'), sum_p=Sum('result_powerka'))
        if agr['cnt'] > 0:
            context['all'] = agr['cnt']
            context['pow_ok'] = agr['sum_p']
            context['pow_no'] = agr['cnt'] - agr['sum_p']
        count_by_day_all = Main.objects.filter(q) \
            .values('date').annotate(my_count_date=Count('date')).annotate(
            result_powerka=Sum('result_powerka')).order_by(('-date'))
        count_by_day_bad = Main.objects.filter(q).filter(result_powerka=0) \
            .values('date').annotate(my_count_date=Count('date')).order_by(('-date'))
        # print(count_by_day_all)

        return (request, 'simpleuser/index.html', context)


class SuperUserClass():

    def create_context(self, request):

        city_object = City.objects.all()
        svidet_object = View_svidet.objects.all()
        fio_worker = User.objects.all()

        if request.method == 'GET':

            if 'page' not in request.GET:
                try:
                    del request.session['query_req']
                    request.session.modified = True
                except: pass

            # print(request.session.get('query_req', '111'), 11111)
            try:
                dict_from_reqest = request.session.get('query_req', [])
                q = createRequestToBDForSuperuser(dict_from_reqest)
                main = Main.objects.filter(q)
                context = ClassPaginator().pagin(request, main)
                context = addContextRequest(context, dict_from_reqest, svidet_object, city_object, fio_worker)
            except:
                q = Q()
                main = Main.objects.filter(q)
                context = ClassPaginator().pagin(request, main)

            context['form'] = MainForm
            context['city_object'] = city_object
            context['svidet_object'] = svidet_object
            context['fio_worker_list'] = fio_worker

        else:
            dict_from_reqest = {}
            for el in request.POST:
                dict_from_reqest[el] = request.POST[el][0] if (type(request.POST[el]) == 'list') else request.POST[el]
            q = createRequestToBDForSuperuser(dict_from_reqest)
            request.session['query_req'] = dict_from_reqest
            main = Main.objects.filter(q)
            context = ClassPaginator().pagin(request, main)
            context = addContextRequest(context, dict_from_reqest, svidet_object, city_object, fio_worker)
            context['form'] = MainForm
        agr = Main.objects.filter(q).aggregate(
            cnt=Count('date'), sum_p=Sum('result_powerka'))
        if agr['cnt'] > 0:
            context['all'] = agr['cnt']
            context['pow_ok'] = agr['sum_p']
            context['pow_no'] = agr['cnt'] - agr['sum_p']
        return (request, 'superuser/index.html', context)


class RevizorClass():
    def create_context(self, request):

        # print (request)
        city_object = City.objects.all()
        svidet_object = View_svidet.objects.all()

        if request.method == 'GET':
            q = Q()
            main = Main.objects.filter(q)
            context = ClassPaginator().pagin(request, main)
            context['form'] = MainForm
            context['city_object'] = city_object
            context['svidet_object'] = svidet_object

        else:
            request.session['date_s'] = request.POST['date_s']
            request.session['date_po'] = request.POST['date_po']
            request.session['search_adr'] = request.POST['search_adr']
            request.session['view_svidet'] = request.POST['view_svidet']
            request.session['city'] = request.POST['city']
            request.session['water'] = request.POST['water']
            request.session['num_fabric'] = request.POST['num_fabric']
            request.session['num_svidet_powerka'] = request.POST['num_svidet_powerka']
            s = request.session['date_s']
            po = request.session['date_po']
            adr = request.session['search_adr']
            view_svidet = request.session['view_svidet']
            c = request.session['city']
            wat = request.session['water']
            num_fabric = request.session['num_fabric']
            num_svidet_powerka = request.session['num_svidet_powerka']

            q = create_request_to_bd(
                s=s, po=po, adr=adr, num_fabric=num_fabric, n_s_v=num_svidet_powerka)
            if wat != '9':
                q = q & Q(hot_water=wat)
            if c != '0':
                q = q & Q(city__city=c)
            if view_svidet != '0':
                q = q & Q(view_svidet__view_svidet=view_svidet)
            #   print (q)
            main = Main.objects.filter(q)
            context = ClassPaginator().pagin(request, main)
            context['date_s'] = s
            context['date_po'] = po
            context['search_adr'] = adr
            context['view_svidet'] = view_svidet
            context['form'] = MainForm
            context['city_object'] = city_object
            context['city'] = c
            context['svidet_object'] = svidet_object
            context['num_fabric'] = num_fabric
            context['num_svidet_powerka'] = num_svidet_powerka
            context['water'] = wat
        agr = Main.objects.filter(q).aggregate(
            cnt=Count('date'), sum_p=Sum('result_powerka'))
        if agr['cnt'] > 0:
            context['all'] = agr['cnt']
            context['pow_ok'] = agr['sum_p']
            context['pow_no'] = agr['cnt'] - agr['sum_p']
        return (request, 'revizoruser/index.html', context)
