from django.urls import path, include
from django.contrib import admin

from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'todos', views.MatrixTodoView, 'todo')

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/newsmail/', include('newsmail.urls')),
    path('api/', include(router.urls)),
]
