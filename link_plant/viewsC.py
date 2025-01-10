from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import CreateView # CreateView: is a View for creating a new object, with a response rendered by a template.
from django.urls import reverse_lazy
from .models import Profile, Link

# Create your views here.

class LinkListview(ListView):
    model = Link
    template_name = "index.html"


class LinkCreateView(CreateView):

    # Specify the model
    model = Link

    # Specify the fields
    fields = "__all__" # This would actually create the form for us, so we wont have to go and create the form in a seperate file, all we just have to do is to specify the fields i.e "__all__"
    
    # Where to send the user after they have successfully created a link
    success_url = reverse_lazy('link-list') # sending them to the home page i.e the LinkListView, 'link-list' is actually the url name for the home page
    
    template_name = "form.html"




# By default it would be looking for a template called model_list.html, in our case -> link_list.html   

# Add the form, reserve url