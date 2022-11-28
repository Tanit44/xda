from django.shortcuts import render,redirect
from app.models import *
from app.forms import *

from django.views import generic
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q

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

# สำหรับ เพิ่ม/แก้ไข/ลบ ทีมงาน
def add_staff(request, id = 0):
  userall = CustomUser.objects.all().order_by('-id') # เรียงจาก หลัง ไป หน้า
  allusertype = UserType.objects.all()
  if request.method == 'GET':
    if id == 0:
      form = AddStaffForm()
      context = {
        'queryset': userall, # show in datatable
        'usertypeall': allusertype, # show in select
        'form': form
      }
      # return render(request, 'admin/add_staff.html', context)
    else: # Edit
      alluser = CustomUser.objects.get(id = id)
      form = AddStaffForm(instance = alluser)
      a_user_t = alluser.user_type # select user_type for ref
      context = {
        'queryset': userall, # show in datatable
        'usertypeall': allusertype, # show in select
        'ausert': a_user_t, # show in selected
        'form': form
      }
    return render(request, 'admin/add_staff.html', context)
  else:
    if id == 0:
      form = AddStaffForm(request.POST)
      if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        form = CustomUser.objects.create_user(
          username = username,
          password = password,
          email = email,
          user_type = user_type,
        )
        form.save()
    else:
      alluser = CustomUser.objects.get(id = id)
      form = AddStaffForm(request.POST, instance = alluser)
      if form.is_valid():
        user = form.save()
        user.set_password(user.password)
        user.save()
    return redirect('/add_staff/')

def delete_staff(request, id):
  alluser = CustomUser.objects.get(id = id)
  alluser.delete()
  return redirect('/add_staff/')

# สำหรับ เพิ่ม/แก้ไข/ลบ คำนำหน้าชื่อ
def add_gender(request, id = 0):
  genderall = Gender.objects.all()
  if request.method == 'GET':
    if id == 0:
      form = AddGenderForm()
    else:
      allgender = Gender.objects.get(id = id)
      form = AddGenderForm(instance = allgender)
    context = {
      'queryset': genderall,
      'form': form
    }
    return render(request, 'admin/add_gender.html', context)
  else:
    if id == 0:
      form = AddGenderForm(request.POST)
    else:
      allgender = Gender.objects.get(id = id)
      form = AddGenderForm(request.POST, instance = allgender)
    if form.is_valid():
      form.save()
    return redirect('/add_gender/')

def delete_gender(request, id):
  allgender = Gender.objects.get(id = id)
  allgender.delete()
  return redirect('/add_gender/')

# สำหรับ เพิ่ม/แก้ไข/ลบ ธรรมวุฒิ
def add_level(request, id = 0):
  levelall = Level.objects.all()
  if request.method == 'GET':
    if id == 0:
      form = AddLevelForm()
    else:
      alllevel = Level.objects.get(id = id)
      form = AddLevelForm(instance = alllevel)
    context = {
      'queryset': levelall,
      'form': form
    }
    return render(request, 'admin/add_level.html', context)
  else:
    if id == 0:
      form = AddLevelForm(request.POST)
    else:
      alllevel = Level.objects.get(id = id)
      form = AddLevelForm(request.POST, instance = alllevel)
    if form.is_valid():
      form.save()
    return redirect('/add_level/')

def delete_level(request, id):
  alllevel = Level.objects.get(id = id)
  alllevel.delete()
  return redirect('/add_level/')

# สำหรับ เพิ่ม/แก้ไข/ลบ อ.ถ่ายทอดเบิกธรรม
def add_pro(request, id = 0):
  proall = Pro.objects.all()
  if request.method == 'GET':
    if id == 0:
      form = AddProForm()
    else:
      allpro = Pro.objects.get(id = id)
      form = AddProForm(instance = allpro)
    context = {
      'queryset': proall,
      'form': form
    }
    return render(request, 'admin/add_pro.html', context)
  else:
    if id == 0:
      form = AddProForm(request.POST)
    else:
      allpro = Pro.objects.get(id = id)
      form = AddProForm(request.POST, instance = allpro)
    if form.is_valid():
      form.save()
    return redirect('/add_pro/')

def delete_pro(request, id):
  allpro = Pro.objects.get(id = id)
  allpro.delete()
  return redirect('/add_pro/')
    
# สำหรับ เพิ่ม/แก้ไข/ลบ การศึกษา
def add_edu(request, id = 0):
    eduall = Edu.objects.all() 
    if request.method == "GET":
        if id == 0:
            form = AddEduForm()
        else:
            alledu = Edu.objects.get(id = id)
            form = AddEduForm(instance = alledu)

        context = {
                'queryset': eduall,
                "form": form
            }
        return render(request, "admin/add_edu.html", context)
    else:
        if id == 0:
            form = AddEduForm(request.POST)
        else:
            alledu = Edu.objects.get(id = id)
            form = AddEduForm(request.POST, instance = alledu)
        if form.is_valid():
            form.save()
        return redirect('/add_edu/')

def delete_edu(request, id):
    alledu = Edu.objects.get(id = id)
    alledu.delete()
    return redirect('/add_edu/')

# สำหรับ เพิ่ม/แก้ไข/ลบ อาชีพ
def add_career(request, id = 0):
    careerall = Career.objects.all() 
    if request.method == "GET":
        if id == 0:
            form = AddCareerForm()
        else:
            allcareer = Career.objects.get(id = id)
            form = AddCareerForm(instance=allcareer)

        context = {
                'queryset': careerall,
                "form": form
            }
        return render(request, "admin/add_career.html", context)
    else:
        if id == 0:
            form = AddCareerForm(request.POST)
        else:
            allcareer = Career.objects.get(id = id)
            form = AddCareerForm(request.POST, instance = allcareer)
        if form.is_valid():
            form.save()
        return redirect('/add_career/')

def delete_career(request, id):
    allcareer = Career.objects.get(id = id)
    allcareer.delete()
    return redirect('/add_career/')

class TableAllsJsonView(BaseDatatableView):
    # Model specification
    model = TableAll
    # Field specification
    columns = ['id', 'nId_person', 'cGender', 'cFname', 'nAge', 'cRoom', 'dDate', 'cPro', 'cRec', 'cSup']

    # Specify search method: Partial match
    # def get_filter_method(self):
    #     return super().FILTER_ICONTAINS

    def filter_queryset(self, qs):
            # use parameters passed in GET request to filter queryset

            # simple example:
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(cFname__istartswith=search) |
                Q(nId_person__istartswith=search)
            )
        return qs

# Base class for printing / Excel / CSV output
class BaseReportView(generic.ListView):
    model = TableAll

    # Get selected data
    def get_queryset(self):
        id_list = self.request.GET['id_list'].split('_')
        result = TableAll.objects.filter(id__in = id_list)
        return result


# Print screen display
class PrintView(BaseReportView):
    template_name = 'admin/print.html'

def tableall_form(request, id = 0):    
    tableall = TableAll.objects.get(id = id)
    dDate = tableall.dDate
    s_cbDd = tableall.cbDd # cbDd for check-box
    form = TableAllForm(instance = tableall)
    context = {
        'dDate' : dDate,
        'form': form,
        's_cbDd' : s_cbDd, # cbDd for check-box
    }
    return render(request, "layouts/tableall_form.html", context)