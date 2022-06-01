from django.contrib import admin
from .models import QR, Data, Attendance
# Register your models here.
admin.site.register(QR)
admin.site.register(Data)
admin.site.register(Attendance)