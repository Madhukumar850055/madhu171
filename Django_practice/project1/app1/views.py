from django.shortcuts import render
from .import models
# Create your views here.
def Person(request):
          p=models.Person.objects.all()
          dict={
                    'per': p,
          }
          return render(request,"person.html",dict)
