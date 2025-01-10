from django.shortcuts import render, get_object_or_404
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


def profile_view(request, profile_slug):

    # Extract the record with the given slug from the primary key table
    profile = get_object_or_404(Profile, slug=profile_slug)

    # Extract the records associated with the 'profile' variable bcos of a field name called 'related_name' = 'links'
    links = profile.links.all() 
    context = {
        'profile': profile,
        'links': links
    }

    return render(request, 'profile.html', context)

def splash_views(request, name):

    profile = get_object_or_404(Profile, name=name)

    splashes = profile.links.all()

    context = {
        'profile': profile,
        'splashes': splashes
    }

    return render(request, 'jo.html', context)
