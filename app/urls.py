from django.urls import path
from . import views, AdminViews 
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
 
]