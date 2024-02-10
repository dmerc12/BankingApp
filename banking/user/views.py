from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser

# Index view
def index(request):
    return render(request, 'index.html')

# Login view 
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {user.first_name}!')
                return redirect('home')
            else:
                messages.error(request, 'Incorrect username or password, please try again!')
                return redirect('login')
        else:
            messages.error(request, 'Incorrect username or password, please try again!')
            return redirect('login')
    else:
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    
# Logout view
def logout_user(request):
    logout(request)
    messages.success(request, 'Goodbye!')
    return redirect('home')

# Register view for users
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            user = form.save()
            CustomUser.objects.create(user=user, phone_number=phone_number)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been successfully registered! Welcome!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})
