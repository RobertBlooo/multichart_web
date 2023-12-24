from django.contrib import admin
from mysite import models

class StrategyAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date', 'commodity', 'settlement')

class CommodityAdmin(admin.ModelAdmin):
    list_display = ('name', 'point_value')

class SessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'trade_time')
admin.site.register(models.Strategy, StrategyAdmin)
admin.site.register(models.Session, SessionAdmin)
admin.site.register(models.Commodity, CommodityAdmin)
