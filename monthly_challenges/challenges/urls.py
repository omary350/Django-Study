from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.Number_monthly_challenges),
    path("<str:month>", views.monthly_challenges, name="month-challenge")
]
