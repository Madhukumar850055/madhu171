from django.shortcuts import render
from . models import Users
from . import forms

# Create your views here.
def home(request):
          return render(request,'app2/index.html')

######
def index(request):
          return render(request,'app2/index.html')

def users(request):
          user_list=Users.objects.all()
          dict1={'users':user_list}
          return render(request,'app2/users.html',context=dict1)

def formView(request):
          form = forms.UserForm()
          if request.method == "Post":
                    form = forms.UserForm(request.POST)
                    if form.is_valid():
                              print("validation success")
                              print("First Name :" + form.cleaned_data['first_name'])
                              print("Last Name :" + form.cleaned_data['last_name'])
                              print("Email :" + form.cleaned_data['email'])

          return render(request,'app2/user_form.html',{'form':form})

