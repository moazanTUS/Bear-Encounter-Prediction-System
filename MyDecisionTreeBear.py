import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

class MyDecisionTreeBear:
    def __init__(self):
        self.df = pd.read_csv('data (3).csv')

        #  whitespace
        self.df.columns = self.df.columns.str.strip()

        #  encoder woudnt work without it
        self.encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')


        self.model = DecisionTreeClassifier()

    def preprocess_data(self, seed_value):
        # Handle unknown categories in 'gender' as was having problems
        self.df['gender'].fillna('Unknown', inplace=True)  #
        self.df['Month'].fillna('Unknown', inplace=True)

        self.X = self.encoder.fit_transform(self.df[['age', 'gender', 'Month', 'Year', 'Type']])
        self.y = self.df['Type of bear']

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=seed_value)

    def trainData(self):
        self.model.fit(self.X_train, self.y_train)

    def testData(self):
        predictions = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, predictions)  # Calculate accuracy


        cm = confusion_matrix(self.y_test, predictions)

        return predictions.tolist(), accuracy, cm

    def makePrediction(self, age, gender, month, year, encounter_type):
        input_data = pd.DataFrame([[age, gender, month, year, encounter_type]], columns=['age', 'gender', 'Month', 'Year', 'Type'])
        encoded_input = self.encoder.transform(input_data)

        prediction = self.model.predict(encoded_input)
        return prediction[0]
