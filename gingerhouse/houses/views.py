from django.views.generic import ListView, DetailView

from gingerhouse.houses.models import GingerHouse


class HousesListView(ListView):
    model = GingerHouse
    template_name = 'houses/index.html'


class HouseDetailView(DetailView):
    model = GingerHouse
    template_name = 'houses/detail.html'
