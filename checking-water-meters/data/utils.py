from django.shortcuts import render, redirect, HttpResponse
from .models import Main, City, DefaultForUser, View_svidet, HistoryGiveSvid,CountForSvidet
from django.contrib.auth.models import User
from django.db.models import Q, Sum, Count

def issuecert(request): 
    
    def_user = DefaultForUser.objects.all()
    
    context = {'svidet_object': View_svidet.objects.all()}
    context['give_svidet'] = HistoryGiveSvid.objects.all().order_by('-id')[:10]
    context['def_user'] = DefaultForUser.objects.all()
    context['fio_worker_list'] = User.objects.all()
    return render(request, 'superuser/issue_certificates.html', context)


def give_svidet(request):
   
    
    left_count_svidet = int(request.POST['left_count_svidet'])
    view_svidet = request.POST['view_svidet']
    fio_worker = request.POST['fio_worker']



    v_s = CountForSvidet.objects.filter(view_svidet__view_svidet=view_svidet).last()
    num_start = v_s.count
    v_s.count = v_s.count + left_count_svidet
    num_end = v_s.count
    

    b = HistoryGiveSvid.objects.filter(view_svidet=view_svidet).filter(fio_worker=fio_worker).last()
    
    if b :
        b.left_count_svidet = str(int(b.left_count_svidet)+ left_count_svidet)
        b.range_number = str(num_start)+'--'+str(num_end-1)
    else:
        b = HistoryGiveSvid(
            fio_worker=fio_worker,
            view_svidet=view_svidet,
            range_number = str(num_start)+'--'+str(num_end-1),
            left_count_svidet= left_count_svidet
            )
    b.save()
    v_s.save()

    return HttpResponse("dsf")
