from django.shortcuts import render,redirect
from . forms import UserInfoForm,UserProfileInfoForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def index(request):
          return render(request,('app4/index.html'))

# def login(request):
#           return render(request,('app4/login.html'))

def register(request):
          registered=False
          if request.method == "POST":
                    user_form= UserInfoForm(data=request.POST)
                    profile_form = UserProfileInfoForm(data=request.POST)
                    if user_form.is_valid() and profile_form.is_valid():
                              user=user_form.save()
                              user.set_password(user.password)
                              user.save()
                              profile=profile_form.save(commit=False)
                              profile.user=user
                              if 'profile_pic' in request.FILES:
                                        profile.profile_pic = request.FILES['profile_pic']
                                        profile.save()
                                        registered=True
                    else:
                              print("Invalid Form")
          else:
                    user_form=UserInfoForm()
                    profile_form=UserProfileInfoForm()
          return render(request,'app4/register.html',{'registered':registered,'user_form':user_form,'profile_form':profile_form})


def user_login(request):
          if request.method=='POST':
                    username = request.POST.get('username')
                    password = request.POST.get('password')
                    user = authenticate(request,username=username,password=password)
                    if user is not None:
                              login(request,user)
                              return redirect('index')
                    else:
                              messages.info(request,'username and password are incorrect')
          context={}
          return render(request,'app4/login.html',context)

def user_logout(request):
          logout(request)
          return redirect('app4:login')
