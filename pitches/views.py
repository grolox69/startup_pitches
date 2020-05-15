from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from .models import Pitch


class PitchListView(ListView):
    model = Pitch
    template_name = 'home.html'


class PitchDetailView(DetailView):
    model = Pitch
    template_name = 'pitch_detail.html'


class SearchResultsListView(ListView):
    model = Pitch
    context_object_name = 'pitch_list'
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Pitch.objects.filter(Q(name__icontains=query) | Q(tags__icontains=query) | Q(pub_date__icontains=query))


class AboutTemplateView(TemplateView):
    template_name = 'about.html'
