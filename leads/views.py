from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView
from .forms import LeadModelForm, AgentModelForm
from .models import Lead, Agent, User


class LeadsList(ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'

    
class LeadCreateView(CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self) -> str:
        return reverse("leads:lead-list")
    
    def form_valid(self, form):
        return super(LeadCreateView, self).form_valid(form)