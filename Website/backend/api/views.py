from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated, AllowAny
from .RandomForest import RandomForestClassifierModel
from .DecisionTree import DecisionTreeClassifierModel
from .serializers import WineSerializer
import pickle

with open('D:/Work/Work/NLP/ML/Wine_Quality_Classification/Website/backend/api/Random_forest_model.pkl', 'rb') as file:
    random_forest = pickle.load(file)


decision_tree = DecisionTreeClassifierModel()

# Create your views here.
class RandomForestPredict(generics.CreateAPIView):
    serializer_class = WineSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        data = request.data
        features = [
            data['fixed_acidity'],
            data['volatile_acidity'],
            data['citric_acid'],
            data['residual_sugar'],
            data['chlorides'],
            data['free_sulfur_dioxide'],
            data['total_sulfur_dioxide'],
            data['density'],
            data['pH'],
            data['sulphates'],
            data['alcohol']
        ]
        prediction = random_forest.predict([features])
        return Response({'quality': prediction[0]})


class DecisionTreePredict(generics.CreateAPIView):
    serializer_class = WineSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        data = request.data
        features = [
            data['fixed_acidity'],
            data['volatile_acidity'],
            data['citric_acid'],
            data['residual_sugar'],
            data['chlorides'],
            data['free_sulfur_dioxide'],
            data['total_sulfur_dioxide'],
            data['density'],
            data['pH'],
            data['sulphates'],
            data['alcohol']
        ]
        prediction = decision_tree.predict([features])
        return Response({'quality': prediction[0]})

    
