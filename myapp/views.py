from django.shortcuts import render
from django.views.generic import TemplateView
import datetime as dt
# Create your views here.

def home(request):
  nowt=dt.datetime.today()
  return render(request,'home.html',{'myname':'reza','rdate':nowt})

class HomeView(TemplateView):
    template_name = 'home.html'
    nowt=dt.datetime.today()
    extra_context = {'myname':'reza','rdate':nowt}