from django.urls import path

from gingerhouse.houses.views import HousesListView, HouseDetailView


app_name = "houses"

urlpatterns = [
    # CASES
    path("", HousesListView.as_view(), name="index"),
    path("houses/<int:upload_id>/", view=HouseDetailView.as_view(), name="detail"),  # Claim upload
]
