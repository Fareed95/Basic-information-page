from django.shortcuts import render
from app1.models import INFORMATION
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'app1/basic.html')
def function1(request):
    first_name = (request.POST.get('firstname','default'))
    last_name = (request.POST.get('lastname','default'))
    email_get = (request.POST.get('email','default'))
    password_get = (request.POST.get('password','default'))
    address1 = (request.POST.get('address1','default'))
    address2 = (request.POST.get('address2','default'))
    city = (request.POST.get('city','default'))
    state = (request.POST.get('State','default'))
    pincode = (request.POST.get('pincode','default'))
    print(first_name,last_name,email_get,password_get,address1,address2,city,state,pincode)
    INFORMATION.objects.all()
    newuser = INFORMATION(firstname = first_name, lastname = last_name,email = email_get,password = password_get, Address1 = address1, Address2 = address2,City = city,State = state, Pin = pincode)
    newuser.save()
    return render(request,'app1/fun.html')