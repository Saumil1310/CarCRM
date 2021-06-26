from django.contrib import admin
from .models import InventoryMaster,CarDocMaster,LeadMaster,CustomerMaster,AdminMaster,SoldCarsMaster,LeadgerMaster

# Register your models here.

ModelField= lambda model: type('Subclass'+model.__name__,(admin.ModelAdmin,),{
	'list_display':[x.name for x in model._meta.fields],	
})

admin.site.register(InventoryMaster,ModelField(InventoryMaster))
admin.site.register(CustomerMaster,ModelField(CustomerMaster))
admin.site.register(LeadMaster,ModelField(LeadMaster))
admin.site.register(CarDocMaster,ModelField(CarDocMaster))
admin.site.register(AdminMaster,ModelField(AdminMaster))
admin.site.register(SoldCarsMaster,ModelField(SoldCarsMaster))
admin.site.register(LeadgerMaster,ModelField(LeadgerMaster))

