from django.db.models import Q, Sum, Count
from django.core.paginator import Paginator
from .forms import MainForm


def create_request_to_bd(**kwargs):
    q = Q()
    if kwargs['s'] != '':
        q = q & Q(date__gte=kwargs['s'])
    if kwargs['po'] != '':
        q = q & Q(date__lte=kwargs['po'])
    if kwargs['adr'] != '':
        q = q & Q(adress__contains=kwargs['adr'])
    if 'view_svidet' in kwargs and kwargs['view_svidet'] != '':
        if kwargs['view_svidet'] == 'СМЛ':
            vs = 8
        elif kwargs['view_svidet'] == 'СО':
            vs = 7
        elif kwargs['view_svidet'] == 'БЛГ':
            vs = 6
        if kwargs['view_svidet'] != '0':
            q = q & Q(view_svidet=vs)
    return q


class ClassPaginator:

    def pagin(self, request, main):
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
