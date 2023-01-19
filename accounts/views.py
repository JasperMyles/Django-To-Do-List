from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def signup_view(request):
    
    form = UserCreationForm()
    
    context = {
        'form': form
    }
    if request.method == 'POST':
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_valid():
            user = filled_form.save()
            login(request, user)
            print('user created')
            return redirect('todo:todo_home')
        
    return render(request, 'accounts/signup.html', context)


def login_view(request):
    
    login_form = AuthenticationForm()
    
    context = {
        'form': login_form
    }
    if request.method == 'POST':
        filled_login_form = AuthenticationForm(data=request.POST)
        print('this ran')
        if filled_login_form.is_valid():
            user = filled_login_form.get_user()
            login(request, user) 
            print('user authenticated')
            return redirect('todo:todo_list')
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('todo:todo_home')