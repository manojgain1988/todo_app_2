
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
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
from TodoApp.models import todo


# # message
from django.contrib import messages

import uuid
from django.db.models import Q

# Create your views here.

@login_required
def home(request):
    current_user = request.user
    all_task= todo.objects.filter(user=current_user)
    if request.method == "POST":
        name = request.POST.get('todo_name')
        New_todo = todo(user=request.user,todo_description=name)
        New_todo.save()
        messages.success(request, "New Task Created !!")
        return redirect ('home')
    
    context={
        'all_task':all_task
    }
    return render(request, 'home.html',context)


@login_required
def update_task(request,id):
    current_user = request.user
    task = todo.objects.get(user=current_user, id=id)
    task.status=True
    task.save()
    messages.success(request, "Task Updated !!") 
    return redirect('home')


@login_required
def delete_task(request,id):
    task = todo.objects.get(user=request.user, id=id)
    task.delete()
    messages.success(request, "Task Deleted !!") 
    return redirect('home')





def login_page(request):
    if request.method == "POST":
        name = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=name).exists():
            messages.error(request, "User not Available")
            return redirect('login')

        user = authenticate(username=name, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "User Logged in Successfully")
            return redirect('home')

        else:
            messages.error(request, "Password is not Match !!")
            return redirect('login')

    return render(request, 'login.html')




@login_required
def logout_page(request):
    logout(request)
    messages.error(request, "Logout Successfull , Please Login Here !")
    return redirect(login_page)




def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if len(password) < 3:
            messages.error(
                request, 'Please Input your Password more then 3 characters.')
            return redirect('register')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User Already Exists')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Exists')
                return redirect('register')

            else:
                obj = User.objects.create_user(
                    username=username, email=email, password=password)
                obj.set_password(password)
                obj.save()
                messages.success(request, 'User Create Successfully')
                return redirect('login')
        else:
            messages.error(request, "Your Password dosen't Match")
            return redirect('register')

    return render(request, 'register.html')



