from django.contrib import admin
from .models import Grain,DomesticOil,OverseaOil,Mineral,MonthlyDomesticOil,MonthlyGrain,MonthlyOverseaOil,MonthlyMineral

admin.site.register(Grain)
admin.site.register(DomesticOil)
admin.site.register(OverseaOil)
admin.site.register(Mineral)
admin.site.register(MonthlyDomesticOil)
admin.site.register(MonthlyGrain)
admin.site.register(MonthlyOverseaOil)
admin.site.register(MonthlyMineral)