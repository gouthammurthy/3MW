from django.views import generic
from .models import Site


class IndexView(generic.ListView):  # For home page with list of sites
    template_name = 'sites/contents.html'

    def get_queryset(self):
        return Site.objects.all()


class DetailView(generic.DetailView):  # For page with details of site
    model = Site
    template_name = 'sites/detail.html'
