from sklearn.tree import DecisionTreeClassifier
import pickle

class DecisionTreeClassifierModel:

    def __init__(self):
        self.model = DecisionTreeClassifier()

    def fit_model(self):
        with open('D:/Work/Work/NLP/ML/Wine_Quality_Classification/Website/backend/api/decision_tree_model.pkl', 'rb') as file:
            self.model = pickle.load(file)

    def predict(self, features):
        return self.model.predict(features)