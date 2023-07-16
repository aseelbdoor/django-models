from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Snack

# Create your views here.
class HomeView(TemplateView):
    template_name="home.html"

class SnackListView(ListView):
    template_name='snack_list.html'
    model=Snack
    context_object_name = "data"

class DetailView(DetailView):
    template_name='snack_detail.html'
    model=Snack