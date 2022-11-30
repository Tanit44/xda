from django.shortcuts import render, redirect
from django.contrib import messages
from . models import *
from . forms import *

from datetime import datetime
from lunarcalendar import Converter, Solar, Lunar, DateNotExist

from django_datatables_view.base_datatable_view import BaseDatatableView
from django.views.generic import FormView
from django.db.models import Q

from django.views.generic import TemplateView

def skw1_home(request):
    total_skw1 = Skw1.objects.count()
    total_skw101 = Skw101.objects.count()
    total_skw102 = Skw102.objects.count()
    total_skw103 = Skw103.objects.count()
    cb3d_count = Skw1.objects.filter(cb3d='True').count() # count cb3d for display
    cbM_count = Skw1.objects.filter(cbM='True').count() # count cb3M for display
    cbS_count = Skw1.objects.filter(cbS='True').count() # count cb3S for display
    cbJ_count = Skw1.objects.filter(cbJ='True').count() # count cb3J for display
    cbJv_count = Skw1.objects.filter(cbJv='True').count() # count cbJv for display
    cbJc_count = Skw1.objects.filter(cbJc='True').count() # count cbJc for display
    context = {
        'total_skw1': total_skw1,
        'total_skw101': total_skw101,
        'total_skw102': total_skw102,
        'total_skw103': total_skw103,
        'cb3d_count' : cb3d_count, # count cb3d for display
        'cbM_count' : cbM_count, # count cbM for display
        'cbS_count' : cbS_count, # count cbS for display
        'cbJ_count' : cbJ_count, # count cbJ for display
        'cbJv_count' : cbJv_count, # count cbJv for display
        'cbJc_count' : cbJc_count, # count cbJc for display
        }
    return render(request,"skw1/skw1_home.html", context)

class Skw1sJsonView(BaseDatatableView):
    # Model specification
    model = Skw1
    # Field specification
    columns = ['id', 'nId_person', 'cGender', 'cFname', 'nAge', 'cRoom', 'dDate', 'cPro', 'cRec', 'cSup', 'Reference_id']

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

class Skw1Filter(TemplateView):
    template_name = 'layouts/table_filter.html'# ใช้ table_filter.html ร่วมกับ กลุ่มต่างๆด้วยกัน

    def get_context_data(self, **kwargs):
        context = super(Skw1Filter, self).get_context_data(**kwargs)
        context['sallgender'] = Gender.objects.all() # gender all for loop -> เพศ
        context['salllevel'] = Level.objects.all() # level all for loop -> ธรรมวุฒิ
        context['salledu'] = Edu.objects.all() # education all for loop -> การศึกษา
        context['sallpro'] = Pro.objects.all() # pro all for loop -> อ.ถ่ายทอดเบิกธรรม
        context['for'] = 'กลุ่ม กบินทร์บุรี' # for header
        context['Pc'] = 'skw1' # for call back if close
        context['cb3d_count'] = Skw1.objects.filter(cb3d='True').count() # count cb3d for display
        context['cbM_count'] = Skw1.objects.filter(cbM='True').count() # count cb3M for display
        context['cbS_count'] = Skw1.objects.filter(cbS='True').count() # count cb3S for display
        context['cbJ_count'] = Skw1.objects.filter(cbJ='True').count() # count cb3J for display
        context['cbJv_count'] = Skw1.objects.filter(cbJv='True').count() # count cbJv for display
        context['cbJc_count'] = Skw1.objects.filter(cbJc='True').count() # count cbJc for display
        return context

# ใช้คู่กับ tableall_filter_nor ค้นหา บุตลากร กบินทร์บุรี
def is_valid_queryparam(param):
    return param != '' and param is not None
# สำหรับ ค้นหา บุตลากร กบินทร์บุรี 
def skw1_filter_nor(request): # get all object
    allgender = Gender.objects.all() # select gender all for loop เพศ
    alllevel = Level.objects.all() # select level all for loop ธรรมวุฒิ
    alledu = Edu.objects.all() # select edu all for loop การศึกษา
    allpro = Pro.objects.all() # select pro all for loop อ.ถ่ายทอดเบิกธรรม

    qs = Skw1.objects.all() # first run query set from Skw3
    gender_query = request.GET.get('gender') # get group 'เพศ' จากหน้า table_filter.html
    level_query = request.GET.get('level') # get title 'ธรรมวุฒิ' จากหน้า table_filter.html
    edu_query = request.GET.get('edu') # get description 'ธรรมกิจ' จากหน้า table_filter.html
    pro_query = request.GET.get('pro') # get item_all_or_course_all 'หัวข้อบรรยาย' จากหน้า table_filter.html
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

    context = {
        # for loop
        'sallgender':allgender, # sent 'sallgender' for loop เพศ
        'salllevel':alllevel, # sent 'salllevel' for loop เชาฉือ, ธรรมวุฒิ
        'salledu':alledu, # sent 'salledu' for loop การศึกษา
        'sallpro': allpro, # sent 'sallpro' for loop อ.ถ่ายทอดเบิกธรรม
        'queryset': qs, # sent 'queryset' for loop datatable       
		
    }
    return render(request, 'skw1/skw1_filter_nor.html', context)

# Sever Side Save/Edit
# skw101 ฝ่าเซิ่ง
class MainViewSkw101(FormView):
    template_name = 'layouts/zone_n.html'
    form_class = Skw101Form
    def get_context_data(self, **kwargs):
        context = super(MainViewSkw101, self).get_context_data(**kwargs)
        context = {
            'header': 'ฝ่าเซิ่ง',
            'ocd': '', ## เปิดฝอถัง
            'home': 'skw1_home',
            'form': 'skw101_form',
            'id_room': 'skw101',
            's': 'skw101s',
        }
        return context

class Skw101sJsonView(BaseDatatableView):
    # model setting
    model = Skw101
    # columns setting
    columns = ['id', 'nId_person', 'cFname', 'cGender', 'nAge', 'cPro', 'dDate', 'cRec', 'cSup', 'cAddress', 'cMtel', 'cHtel', 'cName']

    # Specify search method: Partial match
    def get_filter_method(self):
        return super().FILTER_ICONTAINS

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(cFname__istartswith=search) |
                Q(nId_person__istartswith=search)
            )
        return qs

def skw101_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            last_id = Skw101.objects.all().last()            
            allgender = Gender.objects.all() # gender for loop
            alllevel = Level.objects.all() # level for loop
            allpro = Pro.objects.all() # pro for loop
            alledu = Edu.objects.all() # edu for loop
            allcareer = Career.objects.all() # career for loop

            next_nId_person = int(last_id.nId_person) + 1
            form = Skw101Form()
            context = {
                's_allgender' : allgender, # gender for loop
                's_alllevel' : alllevel, # level for loop
                's_allpro' : allpro, # pro for loop
                's_alledu' : alledu, # edu for loop
                's_allcareer' : allcareer, # career for loop

                'next_nId_person' : str(next_nId_person),
                'header' : 'ฝ่าเซิ่ง',
                'id_room' : 'skw101',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
        else:
            skw101 = Skw101.objects.get(id = id)            
            allgender = Gender.objects.all() # gender for loop
            alllevel = Level.objects.all() # level for loop
            allpro = Pro.objects.all() # pro for loop
            # alledu = Edu.objects.all().order_by('-ename') # edu for loop เรียงจาก หลัง ไป หน้า
            # allcareer = Career.objects.all().order_by('-cname') # career for loop เรียงจาก หลัง ไป หน้า
            alledu = Edu.objects.all().order_by() # edu for loop
            allcareer = Career.objects.all().order_by() # career for loo

            s_Gender = skw101.cGender # gender for selected
            s_Level = skw101.cLevel # level for selected
            s_Pro = skw101.cPro # pro for selected
            s_Edu = skw101.cEdu # edu for selected
            s_Career = skw101.cCareer # career for selected
            s_cbDd = skw101.cbDd # cbDd for check-box

            # lunar calendar
            dDate = skw101.dDate
            sdDate = str(dDate)
            sdDate_obj = datetime.strptime(sdDate, '%Y-%m-%d') 
            year = int(sdDate_obj.strftime('%Y'))
            month = int(sdDate_obj.strftime('%m'))
            dd = int(sdDate_obj.strftime('%d'))
            solar = Solar(year, month, dd)
            solar1 = solar.to_date()
            # print(solar1)
            # print(dDate)
            lunar = Converter.Solar2Lunar(solar)
            lunar1 = str(datetime(lunar.year, lunar.month, lunar.day))[:-9]
            ldDate_obj = datetime.strptime(lunar1, '%Y-%m-%d')
            lunar2 = ldDate_obj.strftime('%Y.%m.%d')
            # print(ldDate_obj.strftime('%Y.%m.%d'))
            # print(lunar2)
            skw101.cDate_dc = lunar2
            # print(d)
            form = Skw101Form(instance = skw101)
            
            context = {
                's_allgender' : allgender, # gender for loop
                's_alllevel' : alllevel, # level for loop
                's_allpro' : allpro, # pro for loop
                's_alledu' : alledu, # edu for loop
                's_allcareer' : allcareer, # career for loop

                's_Gender' : s_Gender, # gender for selected
                's_Level' : s_Level, # level for selected
                's_Pro' : s_Pro, # pro for selected
                's_Edu' : s_Edu, # edu for selected
                's_Career' : s_Career, # career for selected
                's_cbDd' : s_cbDd, # cbDd for check-box

                'dDate' : dDate,
                'lunar1' : str(lunar1), #'%Y-%m-%d'
                'lunar2' : str(lunar2), #'%Y.%m.%d'
                'header' : 'ฝ่าเซิ่ง',
                'id_room' : 'skw101',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
    else:
        if id == 0:
            try:
                user_exists = TableAll.objects.get(cFname=request.POST['cFname']) # For TableAll
                # user_exists = Bkk1001.objects.get(cFname=request.POST['cFname']) # For Bkk1001
                messages.error(request,"ผู้รับธรรมะท่านนี้ รับธรรมะแล้ว !!!")
                return redirect('/skw101_form')
                
            except TableAll.DoesNotExist: # For TableAll
                form = Skw101Form(request.POST)
                form.save()
                messages.success(request,"กด Close เพื่อปิด แล้ว กด Edit เพิ่มข้อมูลต่อไป")
                # return redirect('/bkk1001_form')
                return redirect('/skw101')
        else:
            skw101 = Skw101.objects.get(id = id)
            form = Skw101Form(request.POST,instance=skw101)
            form.save()
            return redirect('/skw101')

def skw101_delete(request, id):
    skw101 = Skw101.objects.get(id = id)
    skw101.delete()
    return redirect('/skw101')
# skw102 ฉืออี
class MainViewSkw102(FormView):
    template_name = 'layouts/zone_n.html'
    form_class = Skw102Form
    def get_context_data(self, **kwargs):
        context = super(MainViewSkw102, self).get_context_data(**kwargs)
        context = {
            'header': 'ฉืออี',
            'ocd': '', ## เปิดฝอถัง
            'home': 'skw1_home',
            'form': 'skw102_form',
            'id_room': 'skw102',
            's': 'skw101s',
        }
        return context

class Skw102sJsonView(BaseDatatableView):
    # model setting
    model = Skw102
    # columns setting
    columns = ['id', 'nId_person', 'cFname', 'cGender', 'nAge', 'cPro', 'dDate', 'cRec', 'cSup', 'cAddress', 'cMtel', 'cHtel', 'cName']

    # Specify search method: Partial match
    def get_filter_method(self):
        return super().FILTER_ICONTAINS

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(cFname__istartswith=search) |
                Q(nId_person__istartswith=search)
            )
        return qs

def skw102_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            last_id = Skw102.objects.all().last()            
            allgender = Gender.objects.all() # gender for loop
            alllevel = Level.objects.all() # level for loop
            allpro = Pro.objects.all() # pro for loop
            alledu = Edu.objects.all() # edu for loop
            allcareer = Career.objects.all() # career for loop

            next_nId_person = int(last_id.nId_person) + 1
            form = Skw102Form()
            context = {
                's_allgender' : allgender, # gender for loop
                's_alllevel' : alllevel, # level for loop
                's_allpro' : allpro, # pro for loop
                's_alledu' : alledu, # edu for loop
                's_allcareer' : allcareer, # career for loop

                'next_nId_person' : str(next_nId_person),
                'header' : 'ฉืออี',
                'id_room' : 'skw102',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
        else:
            skw102 = Skw102.objects.get(id = id)            
            allgender = Gender.objects.all() # gender for loop
            alllevel = Level.objects.all() # level for loop
            allpro = Pro.objects.all() # pro for loop
            # alledu = Edu.objects.all().order_by('-ename') # edu for loop เรียงจาก หลัง ไป หน้า
            # allcareer = Career.objects.all().order_by('-cname') # career for loop เรียงจาก หลัง ไป หน้า
            alledu = Edu.objects.all().order_by() # edu for loop
            allcareer = Career.objects.all().order_by() # career for loo

            s_Gender = skw102.cGender # gender for selected
            s_Level = skw102.cLevel # level for selected
            s_Pro = skw102.cPro # pro for selected
            s_Edu = skw102.cEdu # edu for selected
            s_Career = skw102.cCareer # career for selected
            s_cbDd = skw102.cbDd # cbDd for check-box

            # lunar calendar
            dDate = skw102.dDate
            sdDate = str(dDate)
            sdDate_obj = datetime.strptime(sdDate, '%Y-%m-%d') 
            year = int(sdDate_obj.strftime('%Y'))
            month = int(sdDate_obj.strftime('%m'))
            dd = int(sdDate_obj.strftime('%d'))
            solar = Solar(year, month, dd)
            solar1 = solar.to_date()
            # print(solar1)
            # print(dDate)
            lunar = Converter.Solar2Lunar(solar)
            lunar1 = str(datetime(lunar.year, lunar.month, lunar.day))[:-9]
            ldDate_obj = datetime.strptime(lunar1, '%Y-%m-%d')
            lunar2 = ldDate_obj.strftime('%Y.%m.%d')
            # print(ldDate_obj.strftime('%Y.%m.%d'))
            # print(lunar2)
            skw102.cDate_dc = lunar2
            # print(d)
            form = Skw101Form(instance = skw102)
            
            context = {
                's_allgender' : allgender, # gender for loop
                's_alllevel' : alllevel, # level for loop
                's_allpro' : allpro, # pro for loop
                's_alledu' : alledu, # edu for loop
                's_allcareer' : allcareer, # career for loop

                's_Gender' : s_Gender, # gender for selected
                's_Level' : s_Level, # level for selected
                's_Pro' : s_Pro, # pro for selected
                's_Edu' : s_Edu, # edu for selected
                's_Career' : s_Career, # career for selected
                's_cbDd' : s_cbDd, # cbDd for check-box

                'dDate' : dDate,
                'lunar1' : str(lunar1), #'%Y-%m-%d'
                'lunar2' : str(lunar2), #'%Y.%m.%d'
                'header' : 'ฉืออี',
                'id_room' : 'skw102',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
    else:
        if id == 0:
            try:
                user_exists = TableAll.objects.get(cFname=request.POST['cFname']) # For TableAll
                # user_exists = Bkk1001.objects.get(cFname=request.POST['cFname']) # For Bkk1001
                messages.error(request,"ผู้รับธรรมะท่านนี้ รับธรรมะแล้ว !!!")
                return redirect('/skw102_form')
                
            except TableAll.DoesNotExist: # For TableAll
                form = Skw102Form(request.POST)
                form.save()
                messages.success(request,"กด Close เพื่อปิด แล้ว กด Edit เพิ่มข้อมูลต่อไป")
                # return redirect('/bkk1001_form')
                return redirect('/skw102')
        else:
            skw102 = Skw102.objects.get(id = id)
            form = Skw102Form(request.POST,instance=skw102)
            form.save()
            return redirect('/skw102')

def skw102_delete(request, id):
    skw102 = Skw102.objects.get(id = id)
    skw102.delete()
    return redirect('/skw102')
# skw103 ฉือจิ้ง
class MainViewSkw103(FormView):
    template_name = 'layouts/zone_n.html'
    form_class = Skw103Form
    def get_context_data(self, **kwargs):
        context = super(MainViewSkw103, self).get_context_data(**kwargs)
        context = {
            'header': 'ฉือจิ้ง',
            'ocd': '', ## เปิดฝอถัง
            'home': 'skw1_home',
            'form': 'skw103_form',
            'id_room': 'skw103',
            's': 'skw103s',
        }
        return context

class Skw103sJsonView(BaseDatatableView):
    # model setting
    model = Skw103
    # columns setting
    columns = ['id', 'nId_person', 'cFname', 'cGender', 'nAge', 'cPro', 'dDate', 'cRec', 'cSup', 'cAddress', 'cMtel', 'cHtel', 'cName']

    # Specify search method: Partial match
    def get_filter_method(self):
        return super().FILTER_ICONTAINS

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(cFname__istartswith=search) |
                Q(nId_person__istartswith=search)
            )
        return qs

def skw103_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            last_id = Skw103.objects.all().last()            
            allgender = Gender.objects.all() # gender for loop
            alllevel = Level.objects.all() # level for loop
            allpro = Pro.objects.all() # pro for loop
            alledu = Edu.objects.all() # edu for loop
            allcareer = Career.objects.all() # career for loop

            next_nId_person = int(last_id.nId_person) + 1
            form = Skw103Form()
            context = {
                's_allgender' : allgender, # gender for loop
                's_alllevel' : alllevel, # level for loop
                's_allpro' : allpro, # pro for loop
                's_alledu' : alledu, # edu for loop
                's_allcareer' : allcareer, # career for loop

                'next_nId_person' : str(next_nId_person),
                'header' : 'ฉือจิ้ง',
                'id_room' : 'skw103',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
        else:
            skw103 = Skw103.objects.get(id = id)            
            allgender = Gender.objects.all() # gender for loop
            alllevel = Level.objects.all() # level for loop
            allpro = Pro.objects.all() # pro for loop
            # alledu = Edu.objects.all().order_by('-ename') # edu for loop เรียงจาก หลัง ไป หน้า
            # allcareer = Career.objects.all().order_by('-cname') # career for loop เรียงจาก หลัง ไป หน้า
            alledu = Edu.objects.all().order_by() # edu for loop
            allcareer = Career.objects.all().order_by() # career for loo

            s_Gender = skw103.cGender # gender for selected
            s_Level = skw103.cLevel # level for selected
            s_Pro = skw103.cPro # pro for selected
            s_Edu = skw103.cEdu # edu for selected
            s_Career = skw103.cCareer # career for selected
            s_cbDd = skw103.cbDd # cbDd for check-box

            # lunar calendar
            dDate = skw103.dDate
            sdDate = str(dDate)
            sdDate_obj = datetime.strptime(sdDate, '%Y-%m-%d') 
            year = int(sdDate_obj.strftime('%Y'))
            month = int(sdDate_obj.strftime('%m'))
            dd = int(sdDate_obj.strftime('%d'))
            solar = Solar(year, month, dd)
            solar1 = solar.to_date()
            # print(solar1)
            # print(dDate)
            lunar = Converter.Solar2Lunar(solar)
            lunar1 = str(datetime(lunar.year, lunar.month, lunar.day))[:-9]
            ldDate_obj = datetime.strptime(lunar1, '%Y-%m-%d')
            lunar2 = ldDate_obj.strftime('%Y.%m.%d')
            # print(ldDate_obj.strftime('%Y.%m.%d'))
            # print(lunar2)
            skw103.cDate_dc = lunar2
            # print(d)
            form = Skw101Form(instance = skw103)
            
            context = {
                's_allgender' : allgender, # gender for loop
                's_alllevel' : alllevel, # level for loop
                's_allpro' : allpro, # pro for loop
                's_alledu' : alledu, # edu for loop
                's_allcareer' : allcareer, # career for loop

                's_Gender' : s_Gender, # gender for selected
                's_Level' : s_Level, # level for selected
                's_Pro' : s_Pro, # pro for selected
                's_Edu' : s_Edu, # edu for selected
                's_Career' : s_Career, # career for selected
                's_cbDd' : s_cbDd, # cbDd for check-box

                'dDate' : dDate,
                'lunar1' : str(lunar1), #'%Y-%m-%d'
                'lunar2' : str(lunar2), #'%Y.%m.%d'
                'header' : 'ฉือจิ้ง',
                'id_room' : 'skw103',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
    else:
        if id == 0:
            try:
                user_exists = TableAll.objects.get(cFname=request.POST['cFname']) # For TableAll
                # user_exists = Bkk1001.objects.get(cFname=request.POST['cFname']) # For Bkk1001
                messages.error(request,"ผู้รับธรรมะท่านนี้ รับธรรมะแล้ว !!!")
                return redirect('/skw103_form')
                
            except TableAll.DoesNotExist: # For TableAll
                form = Skw103Form(request.POST)
                form.save()
                messages.success(request,"กด Close เพื่อปิด แล้ว กด Edit เพิ่มข้อมูลต่อไป")
                # return redirect('/bkk1001_form')
                return redirect('/skw103')
        else:
            skw103 = Skw103.objects.get(id = id)
            form = Skw103Form(request.POST,instance=skw103)
            form.save()
            return redirect('/skw103')

def skw103_delete(request, id):
    skw103 = Skw103.objects.get(id = id)
    skw103.delete()
    return redirect('/skw103')
