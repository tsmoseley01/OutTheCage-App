from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def user(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        role=request.POST.get('role')
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken. Please try again.")
                return redirect('register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already in-use. Sign-in instead?")
                return redirect('register/')
            else:
                if role=="Student":
                    user_reg=User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                elif role=="Faculty":
                    user_reg=User.objects.create_superuser(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                messages.info(request, "Successfully created!")
                user_reg.save()
                return redirect('login/')
        else:
            messages.info(request, "Passwords do not match.")
            return redirect('register/')
    return render(request, 'reg.html')

def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, "Login Success!")
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials.")
            return redirect('register/')
    return render(request, 'log.html')
def logout(request):
    auth.logout(request)
    messages.info(request, "Successfully logged out.")
    return redirect('/')