from django.urls import path
from . import views, AdminViews 

urlpatterns = [
    # Admin
    path('', views.ShowLoginPage, name='show_login'),
    path('doLogin', views.doLogin,name="do_login"),
    path('logout_user', views.logout_user,name="logout"),
    path('admin_home', AdminViews.admin_home,name="admin_home"),    
    path("add_user_type/", AdminViews.add_user_type, name="add_user_type"), # เพิ่ม กลุ่มประเภทผู้ใช้งาน
    path("edit_user_type/<int:id>/", AdminViews.add_user_type, name="edit_user_type"),# แก้ไข กลุ่มประเภทผู้ใช้งาน
    path("delete_user_type/<int:id>/", AdminViews.delete_user_type, name="delete_user_type"),# ลบ กลุ่มประเภทผู้ใช้งาน
    path("add_staff/", AdminViews.add_staff, name="add_staff"), # เพิ่ม ทีมงาน
    path("edit_staff/<int:id>/", AdminViews.add_staff, name="edit_staff"),# แก้ไข ทีมงาน
    path("delete_staff/<int:id>/", AdminViews.delete_staff, name="delete_staff"),# ลบ ทีมงาน
 
]