from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
# Create your views here.

def ShowLoginPage(request):
  return render(request, 'login.html')


def doLogin(request):
  if request.method != 'POST':
    return HttpResponse('<h2>Method Not Allowed</h2>')
  else:
    user=EmailBackEnd.authenticate(request, email= request.POST.get('email'), 
    password = request.POST.get('password'))
    if user != None:
      login(request, user)
      if user.user_type == 'Admin':
        return HttpResponseRedirect('admin_home')
      elif user.user_type == 'Bkk1':
        return HttpResponseRedirect(reverse('bkk1_home'))
      elif user.user_type == 'Skw1':
        return HttpResponseRedirect(reverse('skw1_home'))
      elif user.user_type == 'Skw3':
        return HttpResponseRedirect(reverse('skw3_home'))
      else:
        return HttpResponse('User login' + str (user.user_type))
    else:
      # messages.error(request, 'Invalid Login Details')
      return HttpResponseRedirect('/')

def logout_user(request):
  logout(request)
  return HttpResponseRedirect('/')
