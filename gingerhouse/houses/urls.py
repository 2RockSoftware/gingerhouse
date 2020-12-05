from django.urls import path
from django.views.generic import TemplateView

from gingerhouse.houses.views import HousesListView, HouseDetailView, VoteView, VoteDetailView


app_name = "houses"

urlpatterns = [
    path("", HousesListView.as_view(), name="index"),
    path("houses/<int:pk>/", view=HouseDetailView.as_view(), name="detail"),  # ginger house detail
    path("vote/<int:ginger_house_id>/", view=VoteView.as_view(), name="vote"),  # vote endpoint
    path("vote/<int:pk>/detail/", view=VoteDetailView.as_view(), name="vote-detail"),  # vote detail
    path("404", view=TemplateView.as_view(template_name='404.html'), name="test-404"),
]
