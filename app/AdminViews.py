from django.shortcuts import render
from .models import *

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