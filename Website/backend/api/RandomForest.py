from sklearn.ensemble import RandomForestClassifier
import pickle

class RandomForestClassifierModel:

    def __init__(self):
        with open('D:/Work/Work/NLP/ML/Wine_Quality_Classification/Website/backend/api/Random_forest_model.pkl', 'rb') as file:
            self.model = pickle.load(file)

    def predict(self, features):
        return self.model.predict(features)