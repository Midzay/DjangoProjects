from django.urls import path
from .views import *

# from .reports import *


urlpatterns = [
    path('', Index.as_view()),
    #  path('data/',check_user, name='index_data'),
    #  # path('',Index.as_view(template='index.html'), name='index_data'),
     path('update/',update, name='update'),
    path('edit_dispatcher/<int:num_id>/',Edit.as_view(), name='edit_dispatcher'),
     path('del_dispatcher/<int:num_id>/',del_dispatcher, name='del_dispatcher'),
    #  path('protocol/<int:num_id>/',protocol, name='protocol'),
     path('disp_reports/',report_for_dispatcher, name='report_for_dispatcher'),
    # # path('reports/',Index.as_view(template='reports.html'), name='reports'),
    #
     path('disp_reports/',report_for_dispatcher, name='disp_reports'),
    #
    #
    #
    #  path('one_report/',one_report, name='one_report'),
    #  path('worker_report/',MiniReport.as_view(obj_report = 'Work'), name='worker_report'),
    #  path('city_report/',MiniReport.as_view(obj_report = 'City'), name='city_report'),

]
