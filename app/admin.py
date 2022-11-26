from django.contrib import admin

from . models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.site_header = 'ระบบฐานข้อมูลกลาง'

class UserModel(UserAdmin):
  pass

admin.site.register(CustomUser, UserModel)

@admin.register(
  Bkk101, 
  Bkk102, 
  Bkk103, 
  Bkk104, 
  Skw101, 
  Skw102, 
  Skw103, 
  Skw104, 
  Skw301, 
  Skw302, 
  Skw303,
  Skw304,
  Nma101,
  Nma102,
  Nma103,
  Nma104,
  Plk101,
  Plk102,
  Plk103,
  Plk104,
  )

class ViewAdmin(ImportExportModelAdmin):
  pass
