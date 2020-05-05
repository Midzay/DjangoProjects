from django.urls import path
from .views import *

from rest_framework import routers  

urlpatterns = [
    path('settings', get_save_settings),
    path('news', shownewsmail, name='shownewsmail'),
    path('email',get_email , name='get_email'),
]
