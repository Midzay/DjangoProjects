from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Main)
admin.site.register(Place)
admin.site.register(City)
admin.site.register(Method)
admin.site.register(Etalon)
admin.site.register(View_svidet)
admin.site.register(DefaultForUser)
admin.site.register(Interval)

