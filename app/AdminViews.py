from django.shortcuts import render,redirect
from app.models import *
from app.forms import *

def admin_home(request):
  total_all = TableAll.objects.count()
  total_bkk1 = Bkk1.objects.count()
  total_skw1 = Skw1.objects.count()
  context = {
    'total_all': total_all,
    'total_bkk1': total_bkk1,
    'total_skw1': total_skw1,
  }
  return render(request,"admin/admin_home.html", context)

# สำหรับ เพิ่ม/แก้ไข/ลบ กลุ่มประเภทผู้ใช้งาน
def add_user_type(request, id = 0):
  typeall = UserType.objects.all().order_by('-id') # เรียงจาก หลัง ไป หน้า
  if request.method == 'GET':
    if id == 0:
      form = AddUserTypeForm()
    else:
      alltype = UserType.objects.get(pk = id)
      form = AddUserTypeForm(instance = alltype)
    context = {
      'queryset': typeall,
      'form': form
    }
    return render(request, "admin/add_user_type.html", context)
  else:
    if id == 0:
      form = AddUserTypeForm(request.POST)
    else:
      alltype = UserType.objects.get(id = id)
      form = AddUserTypeForm(request.POST, instance = alltype)
    if form.is_valid():
      form.save()
    return redirect("/add_user_type/")

def delete_user_type(request, id):
    alltype = UserType.objects.get(id = id)
    alltype.delete()
    return redirect("/add_user_type/")