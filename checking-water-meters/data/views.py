from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import DefaultForUser
from .forms import MobailForm
from django.views.generic.edit import CreateView, View
from .classforusers import *
from .reports import *


def index_data(request):
    return redirect('/data', permanent=True)


def check_user(request):
    if request.user.is_authenticated:

        if request.user.groups.filter(name='dispatcher').exists():
            return redirect('/dispatcher/')

        elif request.user.groups.filter(name='revizor').exists():
            whoiam = RevizorClass()
            r, s, c = whoiam.create_context(request)
            return render(r, s, c)

        elif request.user.is_staff:
            whoiam = SuperUserClass()
            r, s, c = whoiam.create_context(request)
            return render(r, s, c)
        else:
            whoiam = UserClass()
            r, s, c = whoiam.create_context(request)
            return render(r, s, c)
    else:
        return redirect('/accounts/login/')


def report_for_superuser(request):
    if request.method == "POST" and 'btn_rep' in request.POST:
        return one_report(request)
    elif request.method == "POST" and 'btn_fond' in request.POST:
        return reportForFif(request)
    else:
        whoiam = SuperUserClass()
        r, _, c = whoiam.create_context(request)
        return render(r, 'superuser/reports.html', context=c)


class AddCreateView(View):

    def get(self, request):
        q = Q(user=self.request.user)
        def_user = DefaultForUser.objects.filter(q)
        context ={}
        bound_form = MainForm()
        context['form'] =bound_form
        if len(def_user) > 0:
            context['view_svidet'] = def_user[0].view_svidet
            context['etalon'] = def_user[0].etalon
            context['amp_boolean'] =  def_user[0].amp_boolean
        return render(request, 'add.html', context=context )

    def post(self, request):
        v_s = request.POST['view_svidet']
        n_s = request.POST['num_svidet_powerka']
        date = request.POST['date']
        date_end = request.POST['date_end_powerka']
        check = []
        if n_s.isdigit():
            check  = Main.objects.filter(view_svidet=v_s).filter(num_svidet_powerka=n_s)
        
        bound_form = MainForm(request.POST)
        if bound_form.is_valid() and not check:
            bound_form.save()
            return redirect('/data/')
        return render(request, 'add.html', context={'form': bound_form, 'check': check,'date':date,'date_end':date_end})


class Edit(View):

    def get(self, request, num_id):
        q = Q(user=self.request.user)
        def_user = DefaultForUser.objects.filter(q)
        if len(def_user) > 0:
            amp_boolean =  def_user[0].amp_boolean
        else: amp_boolean =False
        con = Main.objects.get(id=num_id)
        bound_form = MainForm(instance=con)
        return render(request, 'edit.html', context={'form': bound_form, 'con': con,'amp_boolean':amp_boolean})

    def post(self, request, num_id):

        v_s = request.POST['view_svidet']
        n_s = request.POST['num_svidet_powerka']
        
        
        check = []
        flag_check = 0
        if n_s.isdigit():
            check  = Main.objects.filter(view_svidet=v_s).filter(num_svidet_powerka=n_s)
        
        if len(check)>1:
            flag_check = 1
        con = Main.objects.get(id=num_id)
        if len(check)==1 and  not check[0].id==con.id:
            flag_check = 1
        bound_form = MainForm(request.POST, instance=con)
        if bound_form.is_valid() and not flag_check :
            bound_form.save()
            return redirect('/data/')
        return render(request, 'edit.html', context={'form': bound_form,'check':flag_check, 'con': con,})


def del_data(request, num_id):
    main = Main.objects.filter(fio_worker=request.user.last_name)
    if Main.objects.filter(id=num_id).count() != 0:
        rec = Main.objects.get(id=num_id)
        rec.delete()
        return redirect('/data/')
    else:
        return render(request, 'index.html', context={'main': main})


def getRowsForMobile(request, date_row):
    context = {}
    con = Main.objects.filter(fio_worker=request.user.last_name).filter(date=date_row)

    context['con'] = con
    context['mon'] = date_row.split('-')[1]

    return render(request, 'partitions/body/main/mobile-rows-date.html', context)



