from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from map.forms import EmailOrganizationForm
from map import tasks
import json

# Create your views here.
class Home(FormView):
    template_name = "index.html"
    form_class = EmailOrganizationForm
    success_url = '/'

    def form_valid(self, form):
        formjson = json.dumps(form.cleaned_data)
        tasks.send_email.delay(formjson)
        return super().form_valid(form)
