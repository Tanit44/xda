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

def skw3_home(request):
    total_skw3 = Skw3.objects.count()
    total_skw301 = Skw301.objects.count()
    total_skw302 = Skw302.objects.count()
    total_skw303 = Skw303.objects.count()
    cb3d_count = Skw3.objects.filter(cb3d='True').count() # count cb3d for display
    cbM_count = Skw3.objects.filter(cbM='True').count() # count cb3M for display
    cbS_count = Skw3.objects.filter(cbS='True').count() # count cb3S for display
    cbJ_count = Skw3.objects.filter(cbJ='True').count() # count cb3J for display
    cbJv_count = Skw3.objects.filter(cbJv='True').count() # count cbJv for display
    cbJc_count = Skw3.objects.filter(cbJc='True').count() # count cbJc for display
    context = {
        'total_skw3': total_skw3,
        'total_skw301': total_skw301,
        'total_skw302': total_skw302,
        'total_skw303': total_skw303,
        'cb3d_count' : cb3d_count, # count cb3d for display
        'cbM_count' : cbM_count, # count cbM for display
        'cbS_count' : cbS_count, # count cbS for display
        'cbJ_count' : cbJ_count, # count cbJ for display
        'cbJv_count' : cbJv_count, # count cbJv for display
        'cbJc_count' : cbJc_count, # count cbJc for display
        }
    return render(request,"skw3/skw3_home.html", context)

class Skw3sJsonView(BaseDatatableView):
    # Model specification
    model = Skw3
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

class Skw3Filter(TemplateView):
    template_name = 'layouts/table_filter.html'# ใช้ table_filter.html ร่วมกับ กลุ่มต่างๆด้วยกัน

    def get_context_data(self, **kwargs):
        context = super(Skw3Filter, self).get_context_data(**kwargs)
        context['sallgender'] = Gender.objects.all() # gender all for loop -> เพศ
        context['salllevel'] = Level.objects.all() # level all for loop -> ธรรมวุฒิ
        context['salledu'] = Edu.objects.all() # education all for loop -> การศึกษา
        context['sallpro'] = Pro.objects.all() # pro all for loop -> อ.ถ่ายทอดเบิกธรรม
        context['for'] = 'กลุ่ม อรัญประเทศ' # for header
        context['Pc'] = 'skw3' # for call back if close
        context['cb3d_count'] = Skw3.objects.filter(cb3d='True').count() # count cb3d for display
        context['cbM_count'] = Skw3.objects.filter(cbM='True').count() # count cb3M for display
        context['cbS_count'] = Skw3.objects.filter(cbS='True').count() # count cb3S for display
        context['cbJ_count'] = Skw3.objects.filter(cbJ='True').count() # count cb3J for display
        context['cbJv_count'] = Skw3.objects.filter(cbJv='True').count() # count cbJv for display
        context['cbJc_count'] = Skw3.objects.filter(cbJc='True').count() # count cbJc for display
        return context

# ใช้คู่กับ tableall_filter_nor ค้นหา บุตลากร สระแก้ว
def is_valid_queryparam(param):
    return param != '' and param is not None
# สำหรับ ค้นหา บุตลากร สระแก้ว 
def skw3_filter_nor(request): # get all object
    allgender = Gender.objects.all() # select gender all for loop เพศ
    alllevel = Level.objects.all() # select level all for loop ธรรมวุฒิ
    alledu = Edu.objects.all() # select edu all for loop การศึกษา
    allpro = Pro.objects.all() # select pro all for loop อ.ถ่ายทอดเบิกธรรม

    qs = Skw3.objects.all() # first run query set from Skw3
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
    return render(request, 'skw3/skw3_filter_nor.html', context)

# Sever Side Save/Edit
# skw301  
class MainViewSkw301(FormView):
    template_name = 'layouts/zone_n.html'
    form_class = Skw301Form
    def get_context_data(self, **kwargs):
        context = super(MainViewSkw301, self).get_context_data(**kwargs)
        context = {
            'header': 'ซิ่นเต๋อ',
            'ocd': '', ## เปิดฝอถัง
            'home': 'skw3_home',
            'form': 'skw301_form',
            'id_room': 'skw301',
            's': 'skw301s',
        }
        return context

class Skw301sJsonView(BaseDatatableView):
    # model setting
    model = Skw301
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

def skw301_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            last_id = Skw301.objects.all().last()            
            allgender = Gender.objects.all() # gender for loop
            alllevel = Level.objects.all() # level for loop
            allpro = Pro.objects.all() # pro for loop
            alledu = Edu.objects.all() # edu for loop
            allcareer = Career.objects.all() # career for loop

            next_nId_person = int(last_id.nId_person) + 1
            form = Skw301Form()
            context = {
                's_allgender' : allgender, # gender for loop
                's_alllevel' : alllevel, # level for loop
                's_allpro' : allpro, # pro for loop
                's_alledu' : alledu, # edu for loop
                's_allcareer' : allcareer, # career for loop

                'next_nId_person' : str(next_nId_person),
                'header' : 'ซิ่นเต๋อ',
                'id_room' : 'skw301',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
        else:
            skw301 = Skw301.objects.get(id = id)            
            allgender = Gender.objects.all() # gender for loop
            alllevel = Level.objects.all() # level for loop
            allpro = Pro.objects.all() # pro for loop
            # alledu = Edu.objects.all().order_by('-ename') # edu for loop เรียงจาก หลัง ไป หน้า
            # allcareer = Career.objects.all().order_by('-cname') # career for loop เรียงจาก หลัง ไป หน้า
            alledu = Edu.objects.all().order_by() # edu for loop
            allcareer = Career.objects.all().order_by() # career for loo

            s_Gender = skw301.cGender # gender for selected
            s_Level = skw301.cLevel # level for selected
            s_Pro = skw301.cPro # pro for selected
            s_Edu = skw301.cEdu # edu for selected
            s_Career = skw301.cCareer # career for selected
            s_cbDd = skw301.cbDd # cbDd for check-box

            # lunar calendar
            dDate = skw301.dDate
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
            skw301.cDate_dc = lunar2
            # print(d)
            form = Skw301Form(instance = skw301)
            
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
                'header' : 'ซิ่นเต๋อ',
                'id_room' : 'skw301',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
    else:
        if id == 0:
            try:
                user_exists = TableAll.objects.get(cFname=request.POST['cFname']) # For TableAll
                # user_exists = Bkk1001.objects.get(cFname=request.POST['cFname']) # For Bkk1001
                messages.error(request,"ผู้รับธรรมะท่านนี้ รับธรรมะแล้ว !!!")
                return redirect('/skw301_form')
                
            except TableAll.DoesNotExist: # For TableAll
                form = Skw301Form(request.POST)
                form.save()
                messages.success(request,"กด Close เพื่อปิด แล้ว กด Edit เพิ่มข้อมูลต่อไป")
                # return redirect('/bkk1001_form')
                return redirect('/skw301')
        else:
            skw301 = Skw301.objects.get(id = id)
            form = Skw301Form(request.POST,instance=skw301)
            form.save()
            return redirect('/skw301')

def skw301_delete(request, id):
    skw301 = Skw301.objects.get(id = id)
    skw301.delete()
    return redirect('/skw301')
