from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from contact_app.models import Contact

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username__iexact=username).exists():
                messages.error(request,"That username is taken")
                return redirect(reverse('accounts:register'))
            else:
                if User.objects.filter(email__iexact=email).exists():
                    messages.error(request,"That email is being used")
                    return redirect(reverse('accounts:register'))
                else:
                    User.objects.create_user(first_name=first_name,
                                            last_name=last_name,
                                            username=username,
                                            email=email,
                                            password=password)
                    messages.success(request,"Registered. Now you can login")
                    return redirect(reverse('accounts:login'))
        else:
            messages.error(request, 'Passwords must match.')
            return redirect('accounts:register')
    template_name = 'accounts/register.html'
    return render(request,template_name)

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,'Welcome to dashboard')
            return redirect(reverse('accounts:dashboard'))
        else:
            messages.error(request,'Invalid credentials')
            return redirect(reverse('accounts:login'))
    template_name = 'accounts/login.html'
    return render(request,template_name)

@login_required(login_url='/accounts/login/')
def dashboard(request):
    contact_listing = Contact.objects.filter(user_id=request.user.id)
    template_name = 'accounts/dashboard.html'
    context = {'contact_listing':contact_listing,'hello':'hello'}
    return render(request,template_name,context)

def logout_view(request):
    logout(request)
    messages.success(request,"Your'r Logged Out!")
    return redirect(reverse('page_app:home'))
