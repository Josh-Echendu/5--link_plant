from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import CreateView # CreateView: is a View for creating a new object, with a response rendered by a template.
from django.views.generic import UpdateView # View for updating an object, with a response rendered by a template.
from django.views.generic import DeleteView # View for deleting an object retrieved with self.get_object(), with a response rendered by a template.


from django.urls import reverse_lazy
from .models import Profile, Link

# To List your Links 
class LinkListView(ListView):
    model = Link
    template_name = "index.html"

# To Create a Link
class LinkCreateView(CreateView):

    # Specify the model
    model = Link

    # Specify the fields
    fields = "__all__" # This would actually create the form for us, so we wont have to go and create the form in a seperate file, all we just have to do is to specify the fields i.e "__all__"
    
    # Where to send the user after they have successfully created a link
    success_url = reverse_lazy('link-list') # sending them to the home page i.e the LinkListView, 'link-list' is actually the url name for the home page
    template_name = "form.html"

# To Update a Link
class LinkUpdateView(UpdateView):
    model = Link

    # We want the user to only update the text and the url
    fields = ['text', 'url']

    # specify a success url
    success_url = reverse_lazy('link-list')

    # Template
    template_name = "form.html"

class LinkDeleteView(DeleteView):
    model = Link

    success_url = reverse_lazy('link-list')
    
    template_name = "delete.html"




# we deleted a link plant from the webpage