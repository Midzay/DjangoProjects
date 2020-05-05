from django.db.models import Q, Sum, Count
from django.core.paginator import Paginator
from .forms import MainForm
from .models import Main
from django.shortcuts import render, redirect, HttpResponseRedirect


def findRowsForMobile(request, q):
    context = {}
    con = Main.objects.filter(q)
    context['con'] = con
    return (request, 'partitions/body/main/mobile-rows-date.html', context)


def create_request_to_bd(**kwargs):
    q = Q()
    if kwargs['s'] != '':
        q = q & Q(date__gte=kwargs['s'])
    if kwargs['po'] != '':
        q = q & Q(date__lte=kwargs['po'])
    if kwargs['adr'] != '':
        q = q & Q(adress__contains=kwargs['adr'])
    try:
        if kwargs['num_fabric'] != '':
            q = q & Q(num_fabric=kwargs['num_fabric'])
    except:
        pass
    try:
        if kwargs['n_s_v'] != '':
            q = q & Q(num_svidet_powerka=kwargs['n_s_v'])
    except:
        pass
    return q


def createRequestMobile(**kwargs):
    q = Q()
    if kwargs['date'] != '':
        q = q & Q(date=kwargs['date'])
    if kwargs['nsp'] != '':
        q = q & Q(num_svidet_powerka=kwargs['nsp'])
    if kwargs['nf'] != '':
        q = q & Q(num_fabric=kwargs['nf'])
    return q


class PaginatorMobile:

    def pagin(self, request, mobail_main, context):
        #  Пагинатор для  формы
        paginator = Paginator(mobail_main, 40)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['allday'] = len(page)
        good_powerka = 0
        bad_powerka = 0
        for el in page:
            good_powerka += int(el['result_powerka'])
            bad_powerka += int(el['my_count_date']) - int(el['result_powerka'])
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''
        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''
            # Поолучаем агрегатные значения

        mobail_context = {
            'mobail_main': page,
            'mobail_is_paginated': is_paginated,
            'mobail_next_url': next_url,
            'mobail_prev_url': prev_url,
            'good_powerka': good_powerka,
            'bad_powerka': bad_powerka
        }
        context.update(mobail_context)
        return context


class ClassPaginator:

    def     pagin(self, request, main):
        #  Пагинатор для  формы
        paginator = Paginator(main, 50)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''
        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''
            # Поолучаем агрегатные значения

        context = {
            'main': page,
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url
        }
        return context

    def add_context(self, request, main, d_s, d_po, adr, template):
        context = self.pagin(request, main)
        agr = main.aggregate(Sum('result_powerka'), Count('plomba'))
        context['agr'] = agr
        context['date_s'] = d_s
        context['date_po'] = d_po
        context['search_adr'] = adr
        if template == 'reports.html':
            context['form'] = MainForm
        return context


def createRequestToBDForSuperuser(dict_from_reqest):
    q = Q()
    if dict_from_reqest['date_s'] != '':
        q = q & Q(date__gte=dict_from_reqest['date_s'])
    if dict_from_reqest['date_po'] != '':
        q = q & Q(date__lte=dict_from_reqest['date_po'])
    if dict_from_reqest['search_adr'] != '':
        q = q & Q(adress__contains=dict_from_reqest['search_adr'])
    try:
        if dict_from_reqest['num_fabric'] != '':
            q = q & Q(num_fabric__contains=dict_from_reqest['num_fabric'])
    except:
        pass
    try:
        if dict_from_reqest['num_svidet_powerka'] != '':
            q = q & Q(num_svidet_powerka=dict_from_reqest['num_svidet_powerka'])
    except:
        pass
    try:
        if dict_from_reqest['fio_worker'] != '999':
            q = q & Q(fio_worker=dict_from_reqest['fio_worker'])
    except:
        pass
    if dict_from_reqest['water'] != '9':
        q = q & Q(hot_water=dict_from_reqest['water'])
    if dict_from_reqest['city'] != '0':
        q = q & Q(city__city=dict_from_reqest['city'])
    if dict_from_reqest['view_svidet'] != '0':
        q = q & Q(view_svidet__view_svidet=dict_from_reqest['view_svidet'])

    return q


def addContextRequest(context, dict_from_reqest, svidet_object, city_object, fio_worker):
    context['svidet_object'] = svidet_object
    context['city_object'] = city_object
    context['fio_worker_list'] = fio_worker

    context['date_s'] = dict_from_reqest['date_s']
    context['date_po'] = dict_from_reqest['date_po']
    context['search_adr'] = dict_from_reqest['search_adr']

    context['view_svidet'] = dict_from_reqest['view_svidet']
    context['city'] = dict_from_reqest['city']
    context['fw'] = dict_from_reqest['fio_worker']

    context['num_fabric'] = dict_from_reqest['num_fabric']
    context['num_svidet_powerka'] = dict_from_reqest['num_svidet_powerka']
    context['water'] = dict_from_reqest['water']
    return context


def nextPredforMobile(request, curMon, today,dict_month):
    q = Q(fio_worker=request.user.last_name)
    count_by_day_all = Main.objects.filter(q).filter(date__month=int(curMon), date__year=today.year) \
        .values('date').annotate(my_count_date=Count('date')).annotate(
        result_powerka=Sum('result_powerka')).order_by(('-date'))
    context = {}
    context['curMon'] = curMon
    context['month_from_dict'] = dict_month[context['curMon']]
    context = PaginatorMobile().pagin(request, count_by_day_all, context)
    return context
