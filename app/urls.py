from django.urls import path
from . import views, AdminViews, Bkk1Views, Skw3Views
from django.views.generic.base import TemplateView

from app.api import api

urlpatterns = [
    # ninjaAPI
    path('api/', api.urls),
    # Admin
    path('', views.ShowLoginPage, name='show_login'),
    path('doLogin', views.doLogin,name="do_login"),
    path('logout_user', views.logout_user,name="logout"),   
    path("add_user_type/", AdminViews.add_user_type, name="add_user_type"), # เพิ่ม กลุ่มประเภทผู้ใช้งาน
    path("edit_user_type/<int:id>/", AdminViews.add_user_type, name="edit_user_type"),# แก้ไข กลุ่มประเภทผู้ใช้งาน
    path("delete_user_type/<int:id>/", AdminViews.delete_user_type, name="delete_user_type"),# ลบ กลุ่มประเภทผู้ใช้งาน
    path("add_staff/", AdminViews.add_staff, name="add_staff"), # เพิ่ม ทีมงาน
    path("edit_staff/<int:id>/", AdminViews.add_staff, name="edit_staff"),# แก้ไข ทีมงาน
    path("delete_staff/<int:id>/", AdminViews.delete_staff, name="delete_staff"),# ลบ ทีมงาน
    path("add_gender/", AdminViews.add_gender, name="add_gender"), # เพิ่ม เพศ
    path("edit_gender/<int:id>/", AdminViews.add_gender, name="edit_gender"),# แก้ไข เพศ
    path("delete_gender/<int:id>/", AdminViews.delete_gender, name="delete_gender"),# ลบ เพศ
    path("add_level/", AdminViews.add_level, name="add_level"), # เพิ่ม ธรรมวุฒิ
    path("edit_level/<int:id>/", AdminViews.add_level, name="edit_level"),# แก้ไข ธรรมวุฒิ
    path("delete_level/<int:id>/", AdminViews.delete_level, name="delete_level"),# ลบ ธรรมวุฒิ
    path("add_pro/", AdminViews.add_pro, name="add_pro"), # เพิ่ม อ.ถ่ายทอดเบิกธรรม
    path("edit_pro/<int:id>/", AdminViews.add_pro, name="edit_pro"),# แก้ไข อ.ถ่ายทอดเบิกธรรม
    path("delete_pro/<int:id>/", AdminViews.delete_pro, name="delete_pro"),# ลบ อ.ถ่ายทอดเบิกธรรม
    path("add_edu/", AdminViews.add_edu, name="add_edu"), # เพิ่ม การศึกษา
    path("edit_edu/<int:id>/", AdminViews.add_edu, name="edit_edu"),# แก้ไข การศึกษา
    path("delete_edu/<int:id>/", AdminViews.delete_edu, name="delete_edu"),# ลบ การศึกษา
    path("add_career/", AdminViews.add_career, name="add_career"), # เพิ่ม อาชีพ
    path("edit_career/<int:id>/", AdminViews.add_career, name="edit_career"),# แก้ไข อาชีพ
    path("delete_career/<int:id>/", AdminViews.delete_career, name="delete_career"),# ลบ อาชีพ
    # Server-Side admin (view only)
    path('admin_home', AdminViews.admin_home,name="admin_home"), 
    path('tableall', TemplateView.as_view(template_name='layouts/table_all.html'), name='tableall'), # ใช้คู่กับบรรทัดล่าง Server Side for first display
    path('tablealls', AdminViews.TableAllsJsonView.as_view(), name='TableAllsJson'), # use in scripts ใช้คู่กับบรรทัดบน
    path('print', AdminViews.PrintView.as_view(), name='print'),    
    path('tableall_form', AdminViews.tableall_form,name="tableall_form"),
    path('tableall/<int:id>', AdminViews.tableall_form,name="tableall_view"),  
    path('table_filter', AdminViews.TableAllFilter.as_view(), name='table_filter'), # ใช้คู่กับ บรรทัดล่าง Server Side for filter
    path('table_filters', AdminViews.TableAllsJsonView.as_view(), name='TableAllsJson'), # use in scripts ใช้คู่กับบรรทัดบน
    path('table_filter_nor', AdminViews.table_filter_nor, name="table_filter_nor"),  # ค้นหา Normal
    # Server-Side bkk1 (view only)
    path('bkk1_home', Bkk1Views.bkk1_home, name="bkk1_home"),
    path('bkk1', TemplateView.as_view(template_name='layouts/table_all.html'), name='bkk1'),## ใช้คู่กับบรรทัดล่าง Server Side for first display
    path('bkk1s', Bkk1Views.Bkk1sJsonView.as_view(), name='Bkk1sJson'), # use in scripts ใช้คู่กับบรรทัดบน
    path('bkk1_filter', Bkk1Views.Bkk1Filter.as_view(), name='bkk1_filter'), # ใช้คู่กับ บรรทัดล่าง Server Side for filter
    path('bkk1_filters', Bkk1Views.Bkk1sJsonView.as_view(), name='Bkk1sJsonView'), # use in scripts ใช้คู่กับบรรทัดบน
    path('bkk1_filter_nor', Bkk1Views.bkk1_filter_nor, name="bkk1_filter_nor"),  # ค้นหา Normal
    # Sever-Side bkk101 (CRUD)
    path('bkk101', Bkk1Views.MainViewBkk101.as_view(), name='bkk101'),
    path('bkk101s', Bkk1Views.Bkk101sJsonView.as_view(), name='Bkk101sJson'),
    path('bkk101_form', Bkk1Views.bkk101_form,name="bkk101_form"),
    path('bkk101/<int:id>/', Bkk1Views.bkk101_form,name="bkk101_update"),
    path('delete/bkk101/<int:id>/', Bkk1Views.bkk101_delete,name="bkk101_delete"),
   # Sever-Side bkk102 (CRUD)
    path('bkk102', Bkk1Views.MainViewBkk102.as_view(), name='bkk102'),
    path('bkk102s', Bkk1Views.Bkk102sJsonView.as_view(), name='Bkk102sJson'),
    path('bkk102_form', Bkk1Views.bkk102_form,name="bkk102_form"),
    path('bkk102/<int:id>/', Bkk1Views.bkk102_form,name="bkk102_update"),
    path('delete/bkk102/<int:id>/', Bkk1Views.bkk102_delete,name="bkk102_delete"),
    # Sever-Side bkk103 (CRUD)
    path('bkk103', Bkk1Views.MainViewBkk103.as_view(), name='bkk103'),
    path('bkk103s', Bkk1Views.Bkk103sJsonView.as_view(), name='Bkk103sJson'),
    path('bkk103_form', Bkk1Views.bkk103_form,name="bkk103_form"),
    path('bkk103/<int:id>/', Bkk1Views.bkk103_form,name="bkk103_update"),
    path('delete/bkk103/<int:id>/', Bkk1Views.bkk103_delete,name="bkk103_delete"),
    # Server-Side skw3 (view only)
    path('skw3_home', Skw3Views.skw3_home, name="skw3_home"),
    path('skw3', TemplateView.as_view(template_name='layouts/table_all.html'), name='skw3'),
    path('skw3s', Skw3Views.Skw3sJsonView.as_view(), name='Skw3sJson'),
    path('skw3_filter', Skw3Views.Skw3Filter.as_view(), name='skw3_filter'), # ใช้คู่กับ บรรทัดล่าง Server Side 
    path('skw3_filters', Skw3Views.Skw3sJsonView.as_view(), name='Skw3sJsonView'), # use in scripts ใช้คู่กับบรรทัดบน
    path('skw3_filter_nor', Skw3Views.skw3_filter_nor, name="skw3_filter_nor"),  # ค้นหา Normal
     # Sever-Side skw301 (CRUD)
    path('skw301', Skw3Views.MainViewSkw301.as_view(), name='skw301'),
    path('skw301s', Skw3Views.Skw301sJsonView.as_view(), name='Skw103sJson'),
    path('skw301_form', Skw3Views.skw301_form,name="skw301_form"),
    path('skw301/<int:id>/', Skw3Views.skw301_form,name="skw301_update"),
    path('delete/skw301/<int:id>/', Skw3Views.skw301_delete,name="skw301_delete"),

]