from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import DirectoryFactorRel, TDirectoryCode, TFactorCode


admin.site.register(DirectoryFactorRel)
admin.site.register(TDirectoryCode)
admin.site.register(TFactorCode)