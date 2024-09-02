from django.urls import path
from . import views

urlpatterns = [
    path("random_forest_classifier/", views.RandomForestPredict.as_view(),name= "random_forest_classifier"),
    path("decision_tree_classifier/", views.DecisionTreePredict.as_view(), name= "decision_tree_classifier"),
]