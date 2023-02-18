from django.shortcuts import render,HttpResponse
from .models import User
from . import forms
# Create your views here.

def index(request):
          return HttpResponse("<h1>hello Project3<h1>")

def user(request):
          user_list = User.objects.all()
          dict1={'user':user_list}
          return render(request,'app3/users.html',context=dict1)

def formView(request):
          form = forms.UserForm()
          if request.method == 'POST':
                    form =forms.UserForm(request.POST)
                    if form.is_valid():
                              print("Validation Success")
                              print("First Name :" + form.cleaned_data['first_name'])
                              print("Last Name :" +form.cleaned_data['last_name'])
                              print("Email :" + form.cleaned_data['Email'])
          
          return render(request,'app3/user_form.html',{'form':form})


