from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .RandomForest import RandomForestClassifierModel
from .DecisionTree import DecisionTreeClassifierModel
from .serializers import WineSerializer

random_forest = RandomForestClassifierModel()
random_forest.fit_model()

decision_tree = DecisionTreeClassifierModel()
decision_tree.fit_model()

# Create your views here.
class RandomForestPredict(generics.RetrieveAPIView):
    serializer_class = WineSerializer
    lookup_field = 'random_forest'
    permission_classes = [AllowAny]

    def get_queryset(self):
        x_pred = self.kwargs.get(lookup_field)
        y_pred = random_forest.predict(x_pred) 
        return y_pred


class DecisionTreePredict(generics.RetrieveAPIView):
    serializer_class = WineSerializer
    lookup_field = 'random_forest'
    permission_classes = [AllowAny]

    def get_queryset(self):
        x_pred = self.kwargs.get(lookup_field)
        y_pred = random_forest.predict(x_pred) 
        return y_pred

    
