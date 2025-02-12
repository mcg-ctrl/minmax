from django.urls import path

from . import views
from main.views import FoodItemListView

app_name = "main"
urlpatterns = [

    # Default page, e.g. /main/
    path("", views.menu, name="menu"),

    # Details for a food item by id, e.g. /5/
    path("<int:fooditem_id>/", views.details, name="details"),

    # Details for a food item by id, e.g. /5/main/
    path("<int:fooditem_id>/main/", views.details, name="details"),

    # Details for a food item by id, e.g. /main/5/details
    path("<int:fooditem_id>/details/", views.details, name="details"),

    # Placeholder page
    # Results for a food item by id, e.g. /main/5/results/
    path("<int:fooditem_id>/results/", views.results, name="results"),

    # Form for entering a new food item, e.g. /enter/
    path("enter/", views.enter, name="enter"),

    # Form for entering a new food item, e.g. /enter/
    path("list/", views.list, name="list"),

    # Form for entering a new food item, e.g. /enter/
    path("listview/", FoodItemListView.as_view()),

    # List all food items
    path("table/", views.table, name="table")
]