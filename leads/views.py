from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import AgentModelForm, LeadModelForm
from .models import Lead, Agent


# Agnets
class AgentsList(ListView):
    template_name = 'agents/agent_list.html'
    queryset = Agent.objects.all()
    context_object_name = 'agents'

class AgentDetailView(DetailView):
    template_name = "agents/agent_detail.html"
    queryset = Agent.objects.all()
    context_object_name = 'agent'
    
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

def LeadsCreateView(request, pk):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        age = request.POST['age']
        email = request.POST['email']
        agent = Agent.objects.get(id=pk)

        Lead.objects.create(first_name=first_name,
                            last_name=last_name,
                            age=age,
                            email=email,
                            agent=agent)
        
        return redirect("leads:lead-list")
    
    return render(request, 'leads/lead_create.html')

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
