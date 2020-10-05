from django.shortcuts import render
from django.views.generic import FormView
from map.forms import EmailOrganizationForm

# Create your views here.
class Home(FormView):
    template_name = "index.html"
    form_class = EmailOrganizationForm
