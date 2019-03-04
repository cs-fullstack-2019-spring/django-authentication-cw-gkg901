from django.http import HttpResponse
from django.shortcuts import render
from .models import FitnessModel
from .forms import NewUserForm
from django.contrib.auth.models import User


# Create your views here.
# RENDERS TO INDEX.HTML
def index(request):
    return render(request, 'authCWapp/index.html')


# INJECTS FORM INTO NEWUSER.HTML
def newUser(request):
    form = NewUserForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request, 'authCWapp/newUser.html', context)


# CREATES USER IN DATABASE FROM POST
def gotUserInfo(request):
    print(request.POST)
    print(request.POST['username'])
    User.objects.create_user(request.POST['username'], "", "")
    return HttpResponse('REGISTERED')
