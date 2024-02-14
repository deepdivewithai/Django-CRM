from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView
# from .forms import SignUpForm
# from .models import SignUp

# class SignUp(CreateView):
#     template_name = "authenticate/signup.html"
#     form_class = SignUpForm

#     def get_success_url(self) -> str:
#         return reverse("leads:lead-list")
    
#     def form_valid(self, form):
#         return super().form_valid(form)
    

# def SignUp(request):
#     form = SignUpForm()
#     print(request.POST)

#     context = {
#         'form': form
#     }

#     return render(request, 'authenticate/signup.html', context)

    
    
