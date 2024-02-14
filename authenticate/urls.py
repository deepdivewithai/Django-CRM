from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('login/', views.LogIn, name='login'),
    path('logout/', views.LogOut, name='logout'),
    path('activate/<uid64>/<token>', views.activate, name='activate'),
]
