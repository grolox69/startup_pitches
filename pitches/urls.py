from django.urls import path
from .views import PitchListView, PitchDetailView, SearchResultsListView, AboutTemplateView

urlpatterns = [
    path('', PitchListView.as_view(), name='home'),
    path('pitch/<int:pk>/', PitchDetailView.as_view(), name='pitch_detail'),
    path('results/', SearchResultsListView.as_view(), name='pitch_results'),
    path('about/', AboutTemplateView.as_view(), name='about')
]
