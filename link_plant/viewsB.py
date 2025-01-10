from django.shortcuts import render
from django.views.generic import ListView

from .models import Profile, Link

# Create your views here.

class LinkListview(ListView):
    model = Link
    template_name = "index.html"


# By default it would be looking for a template called model_list.html, in our case -> link_list.html   

# Listing Out the Links with a Class Based View ListView