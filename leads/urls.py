from django.urls import path
from . import views

app_name = 'leads'

urlpatterns = [
    path('', views.LeadsList.as_view(), name='lead-list'),
    path('agent-list/', views.AgentsList.as_view(), name='agent-list'),
    path('<int:pk>/', views.LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/delete', views.LeadDeleteView.as_view(), name='lead-delete'),
    path('<int:pk>/update', views.LeadUpdateView.as_view(), name='lead-update'),
    path('lead-create/', views.LeadCreateView.as_view(), name='lead-create'),
    path('agent-create/', views.AgentCreateView.as_view(), name='agent-create'),
]
