from django.urls import path
from .views import *
from .reports import *

urlpatterns = [
    path('', check_user),
    path('data/', check_user, name='index_data'),
    path('create/', AddCreateView.as_view(), name='create_data'),
    path('edit/<int:num_id>/', Edit.as_view(), name='edit_data'),
    path('del/<int:num_id>/', del_data, name='del_data'),
    path('protocol/<int:num_id>/', protocol, name='protocol'),
    path('getrowmobile/<str:date_row>/', getRowsForMobile, name='getRowsForMobile'),
    path('reports/', report_for_superuser, name='reports'),
    path('one_report/', one_report, name='one_report'),
    path('worker_report/', MiniReport.as_view(obj_report='Work'), name='worker_report'),
    path('city_report/', MiniReport.as_view(obj_report='City'), name='city_report'),
    path('check/', check_data, name='check'),
    path('print_many_protokol/', many_protokol, name='print_many_protokol'),
    path('check_svidet/', check_number_svidet, name='check_svidet'),

]
