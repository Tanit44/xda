from django.urls import path
from . import views, AdminViews 

urlpatterns = [
    path('', views.ShowLoginPage, name='show_login'),
    path('doLogin', views.doLogin,name="do_login"),
    path('logout_user', views.logout_user,name="logout"),
    path('admin_home', AdminViews.admin_home,name="admin_home"),
]