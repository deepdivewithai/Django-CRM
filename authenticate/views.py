from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from leads.models import Agent
from django.contrib.auth import authenticate,login,logout

from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from .tokens import generate_token

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

        # Welcome Email

        subject = "Welcome to DJAuth- Django Login!!!"
        message = "Hello " + myuser.first_name + " !!! \n" + "Welcome to DJAuth!!! \nThank You For Visiting Our Website \nWe have also send you a confirmation email, please confirm your email address to activate your account. \n\nThanking You \n\nErnesti!!!"

        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=False)
        print(from_email,"\n",to_list[0])

        # Email Adress Confirmation Email

        current_site = get_current_site(request)
        email_subject = "Confirm your email @ DJAuth- Django Login!!!"
        message2 = render_to_string("email_confirmation.html",{
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })

        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )

        email.fail_silently = True
        email.send()

        return redirect("auth:login")

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
    
def activate(request, uid64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        myuser = Agent.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Agent.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return render(request, 'landing_page.html')


    else:
        return render(request, 'activation_failed.html')