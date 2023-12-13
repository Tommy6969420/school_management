from django.contrib import admin
from.models import ClassBills, Billing,TransportRoutes,Months
# Register your models here.
admin.site.register(ClassBills)
admin.site.register(Billing)
# admin.site.register(TransportRoutes)
admin.site.register(Months)
class TransportRoutesModelAdmin(admin.ModelAdmin):
    ordering=("transport_fee",)
admin.site.register(TransportRoutes,TransportRoutesModelAdmin)