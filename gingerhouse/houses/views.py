from django.shortcuts import redirect, reverse
from django.views.generic import ListView, DetailView, FormView

from gingerhouse.houses.forms import VoteForm
from gingerhouse.houses.models import GingerHouse, Vote


class HousesListView(ListView):
    model = GingerHouse
    template_name = 'houses/index.html'


class HouseDetailView(DetailView):
    model = GingerHouse
    template_name = 'houses/detail.html'
    context_object_name = "house"
    
    def get_context_data(self, **kwargs):
        ctx = super(HouseDetailView, self).get_context_data(**kwargs)
        ctx["form"] = VoteForm(ginger_house=ctx["object"])
        return ctx


class VoteView(FormView):
    template_name = 'houses/detail.html'
    form_class = VoteForm
    
    def get_ginger_house(self):
        ginger_house_id = self.kwargs.get("ginger_house_id")
        ginger_house = GingerHouse.objects.get(pk=ginger_house_id)
        return ginger_house

    def form_valid(self, form):
        ginger_house = self.get_ginger_house()
        vote = Vote.objects.create(email=form.cleaned_data.get("email"), ginger_house=ginger_house)
        return redirect(reverse("houses:vote-detail", kwargs={"pk": vote.id}))

    def get_form_kwargs(self):
        kwargs = super(VoteView, self).get_form_kwargs()
        kwargs['ginger_house'] = self.get_ginger_house()
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super(VoteView, self).get_context_data(**kwargs)
        ctx["house"] = self.get_ginger_house()
        return ctx


class VoteDetailView(DetailView):
    model = Vote
    template_name = 'houses/vote.html'
