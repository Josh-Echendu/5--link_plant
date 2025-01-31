from django.urls import path

from .views import LinkListView, LinkCreateView, profile_view, LinkUpdateView, LinkDeleteView, splash_views

urlpatterns = [
    path('', LinkListView.as_view(), name='link-list'),
    path('link/create/', LinkCreateView.as_view(), name='link-create'),
    path('link/<int:pk>/update/', LinkUpdateView.as_view(), name='link-update'),
    path('link/<int:pk>/delete/', LinkDeleteView.as_view(), name='link-delete'),
    # it is accepting a slug field as a profile_slug varaiable
    path('<slug:profile_slug>/', profile_view, name='profile'),
    path('link/<str:name>/name/', splash_views, name='link-splashes')
]
