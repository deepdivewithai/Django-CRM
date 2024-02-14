from django import forms
from .models import Lead, Agent

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'email',
            'agent'
        )

class AgentModelForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'username',
            'email',
            'password',
        )