from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import AgentModelForm, LeadModelForm
from .models import Lead, Agent


# Agnets
class AgentsList(ListView):
    template_name = 'agents/agent_list.html'
    queryset = Agent.objects.all()
    context_object_name = 'agents'
    
class AgentCreateView(CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return reverse("leads:agent-list")
    
    def form_valid(self, form):
            return super().form_valid(form)

# Leads

class LeadsList(ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'

class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = 'lead'
     
class LeadCreateView(CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self) -> str:
        return reverse("leads:lead-list")
    
    def form_valid(self, form):
        return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self) -> str:
        return reverse("leads:lead-detail", kwargs={'pk': self.object.pk})

class LeadDeleteView(DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self) -> str:
        return reverse("leads:lead-list")
