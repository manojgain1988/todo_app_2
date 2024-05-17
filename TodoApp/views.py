# from django.shortcuts import render, redirect
# from TodoApp.views import login ,register, logout
# from django .contrib import messages
# from django.contrib.auth.models import User



from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

# VIEW
from django.views.generic import CreateView, ListView, DetailView, UpdateView, View, TemplateView, DeleteView

# # Authentication
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# # Login MIXIN
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
# from account.mixins import LogoutRequiredMixin

# # forms
from django.contrib.auth.forms import AuthenticationForm

# # models
from django.contrib.auth.models import User


# # message
from django.contrib import messages

import uuid
from django.db.models import Q

# Create your views here.


def home(request):

    context = {

    }
    return render(request, 'home.html', context)


def about(request):

    context = {

    }
    return render(request, 'about.html', context)


def contact(request):

    context = {

    }
    return render(request, 'contact.html', context)


def login(request):

    context = {

    }
    return render(request, 'login.html', context)


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if len(password) < 3:
            messages.error(request, 'Please Input your Password more then 3 characters.')
            return redirect('register')
        
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User Already Exists')
                return redirect('register')
        
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Exists')
                return redirect('register')
            
            else:
                obj =User.objects.create_user(username=username,email=email,password=password)
                obj.set_password(password)
                obj.save()
                messages.success(request, 'User Create Successfully')
                return redirect('login')
        else:
            messages.error(request, "Your Password dosen't Match")
            return redirect('register')
            


    # context={

    # }
    return render(request, 'register.html')


def logout(request):

    context = {

    }
    return render(request, 'logout.html', context)
