from django.urls import path
from . import views

app_name = 'leads'

urlpatterns = [
    path('', views.LeadsList.as_view(), name='lead-list'),
    path('create/', views.LeadCreateView.as_view(), name='lead-create'),
]
