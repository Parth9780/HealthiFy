from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Register_Form)

class AppointmentData(admin.ModelAdmin):
    list_display=['id','Name','Mobile','Date']
admin.site.register(Appointment,AppointmentData)

admin.site.register(ContactUs)

class AdminData(admin.ModelAdmin):
    list_display=['id','UserName','Email']
admin.site.register(AdminLogin,AdminData)