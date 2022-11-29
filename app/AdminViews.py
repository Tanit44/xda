from django.shortcuts import render,redirect
from app.models import *
from app.forms import *

from django.views import generic
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q

from django.views.generic import TemplateView

def admin_home(request):
  total_all = TableAll.objects.count()
  total_bkk = Bkk.objects.count()
  total_skw = Skw.objects.count()
  cb3d_count = TableAll.objects.filter(cb3d='True').count() # count cb3d for display
  cbM_count = TableAll.objects.filter(cbM='True').count() # count cb3M for display
  cbS_count = TableAll.objects.filter(cbS='True').count() # count cb3S for display
  cbJ_count = TableAll.objects.filter(cbJ='True').count() # count cb3J for display
  cbJv_count = TableAll.objects.filter(cbJv='True').count() # count cbJv for display
  cbJc_count = TableAll.objects.filter(cbJc='True').count() # count cbJc for display

  context = {
    'total_all': total_all, #ทั้งหมด
    'total_bkk': total_bkk, #กทม
    'total_skw': total_skw, #สระแก้ว
    'cb3d_count' : cb3d_count, # count cb3d for display
    'cbM_count' : cbM_count, # count cbM for display
    'cbS_count' : cbS_count, # count cbS for display
    'cbJ_count' : cbJ_count, # count cbJ for display
    'cbJv_count' : cbJv_count, # count cbJv for display
    'cbJc_count' : cbJc_count, # count cbJc for display

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

# Filter
class TableAllFilter(TemplateView):
    template_name = 'layouts/table_filter.html'# ใช้ table_filter.html ร่วมกับ กลุ่มต่างวด้วยกัน

    def get_context_data(self, **kwargs):
        context = super(TableAllFilter, self).get_context_data(**kwargs)
        context['sallgender'] = Gender.objects.all() # gender all for loop -> เพศ
        context['salllevel'] = Level.objects.all() # level all for loop -> ธรรมวุฒิ
        context['salledu'] = Edu.objects.all() # education all for loop -> การศึกษา
        context['sallpro'] = Pro.objects.all() # pro all for loop -> อ.ถ่ายทอดเบิกธรรม
        context['for'] = 'รวม' # for header
        context['Pc'] = 'tableall' # for call back if close
        context['cb3d_count'] = TableAll.objects.filter(cb3d='True').count() # count cb3d for display
        context['cbM_count'] = TableAll.objects.filter(cbM='True').count() # count cb3M for display
        context['cbS_count'] = TableAll.objects.filter(cbS='True').count() # count cb3S for display
        context['cbJ_count'] = TableAll.objects.filter(cbJ='True').count() # count cb3J for display
        context['cbJv_count'] = TableAll.objects.filter(cbJv='True').count() # count cbJv for display
        context['cbJc_count'] = TableAll.objects.filter(cbJc='True').count() # count cbJc for display
        return context

# ใช้คู่กับ tableall_filter_nor ค้นหา บุตลากร รวม
def is_valid_queryparam(param):
    return param != '' and param is not None
# สำหรับ ค้นหา บุตลากร รวม 
def table_filter_nor(request): # get all object
    allgender = Gender.objects.all() # select gender all for loop เพศ
    alllevel = Level.objects.all() # select level all for loop ธรรมวุฒิ
    alledu = Edu.objects.all() # select edu all for loop การศึกษา
    allpro = Pro.objects.all() # select pro all for loop อ.ถ่ายทอดเบิกธรรม

    qs = TableAll.objects.all() # first run query set from TableAll
    gender_query = request.GET.get('gender') # get group 'เพศ' จากหน้า table_filter.html
    level_query = request.GET.get('level') # get title 'ธรรมวุฒิ' จากหน้า table_filter.html
    edu_query = request.GET.get('edu') # get description 'ธรรมกิจ' จากหน้า table_filter.html
    pro_query = request.GET.get('pro') # get pro 'อ.ถ่ายทอดเบิกธรรม' จากหน้า table_filter.html
    pt_query = request.GET.get('pt') # get pt 'ปณืธาน' จากหน้า table_filter.html
    cb3d_query = request.GET.get('cb3d') # get pt '3 วัน' จากหน้า table_filter.html
    cbM_query = request.GET.get('cbM') # get pt 'หมิงเต๋อ' จากหน้า table_filter.html
    cbS_query = request.GET.get('cbS') # get pt 'ซินหมิน' จากหน้า table_filter.html
    cbJ_query = request.GET.get('cbJ') # get pt 'จื่อซั่น' จากหน้า table_filter.html
    cbJv_query = request.GET.get('cbJv') # get pt 'เจี่ยงเอวี๋ยน' จากหน้า table_filter.html
    cbJc_query = request.GET.get('cbJc') # get pt 'เจี่ยงซือ' จากหน้า table_filter.html
    # ***** filter after get data *****
    if is_valid_queryparam(gender_query) and gender_query != 'กรุณาเลือก...': # query set 'gender' เพศ
        qs =qs.filter(cGender=gender_query)
    if is_valid_queryparam(level_query) and level_query != 'กรุณาเลือก...': # query set 'level' ธรรมวุฒิ
        qs =qs.filter(cLevel=level_query)
    if is_valid_queryparam(edu_query) and edu_query != 'กรุณาเลือก...': # query set 'edu' การศึกษา
        qs =qs.filter(cEdu=edu_query)
    if is_valid_queryparam(pro_query) and pro_query != 'กรุณาเลือก...': # query set 'pro' อ.ถ่ายทอดเบิกธรรม
        qs =qs.filter(cPro=pro_query)
    if is_valid_queryparam(pt_query) and pt_query != 'กรุณาเลือก...': # query set 'pt' ปณืธาน
        qs =qs.filter(Q(cPt3=pt_query) # use OR (|) sign ปณืธาน ข้อที่ 3
            | Q(cPt4=pt_query) # ปณืธาน ข้อที่ 4
            | Q(cPt5=pt_query) # ปณืธาน ข้อที่ 5
            | Q(cPt6=pt_query) # ปณืธาน ข้อที่ 6
            ).distinct()
    if cb3d_query == 'on': # query set 'cb3d' true 3 วัน
        qs = qs.filter(cb3d=True)
    if cbM_query == 'on': # query set 'cbM' true หมิงเต๋อ
        qs = qs.filter(cbM=True)
    if cbS_query == 'on': # query set 'cbS' true ซินหมิน
        qs = qs.filter(cbS=True)
    if cbJ_query == 'on': # query set 'cbJ' true จื่อซั่น
        qs = qs.filter(cbJ=True)
    if cbJv_query == 'on': # query set 'cbJv' true เจี่ยงเอวี๋ยน
        qs = qs.filter(cbJv=True)
    if cbJc_query == 'on': # query set 'cbM' true เจี่ยงซือ
        qs = qs.filter(cbJc=True)
    
	  # users = TableAll.objects.all()
	 
        
    context = {
        # for loop
        'sallgender':allgender, # sent 'sallgender' for loop เพศ
        'salllevel':alllevel, # sent 'salllevel' for loop เชาฉือ, ธรรมวุฒิ
        'salledu':alledu, # sent 'salledu' for loop การศึกษา
        'sallpro': allpro, # sent 'sallpro' for loop อ.ถ่ายทอดเบิกธรรม
        'queryset': qs, # sent 'queryset' for loop datatable
    }
    return render(request, 'layouts/table_filter_nor.html', context)
