from django.contrib import admin
from.models import*
# Register your models here.
admin.site.register(Employeetask)

#define ModelAdminclasstatuss
class Employeetask(admin.ModelAdmin):
      list_display=['name','contact','gender','joiningdate','status']
      list_filter=['status','cat']
      

#admin.site.register(Product,ProductAdminClass) 
#admin.site.site_header="Ekart Dashboard"   

