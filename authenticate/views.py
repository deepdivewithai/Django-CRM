from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from leads.models import Agent
from django.contrib.auth import authenticate,login,logout

def SignUp(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric !!!")
            return redirect("auth:signup")
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!!!")
            return redirect("auth:signup")
        
        if Agent.objects.filter(email=email):
            messages.error(request, "Email is already registered!!!")
            return redirect("auth:signup")

        if Agent.objects.filter(username=username):
            messages.error(request, "Please use different Username!!!")
            return redirect("auth:signup")

        myuser = Agent.objects.create_user(username=username, email=email, password=pass1)

        myuser.first_name = first_name
        myuser.last_name = last_name

        myuser.save()

    return render(request, 'authenticate/signup.html')

def LogIn(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            name = user.username
            login(request, user)
            return render(request, 'landing_page.html', context={'name': name})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')
                
    return render(request, 'authenticate/login.html')


def LogOut(request):
    logout(request)
    return redirect("home")
    
