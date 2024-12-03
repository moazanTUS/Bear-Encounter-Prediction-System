# Bear-Encounter-Prediction-System
This project predicts the type of bear involved in an encounter based on input data. It integrates machine learning with a user-friendly GUI for training, testing, and making predictions.
Core Components
GUI (gui.py):

Built using Tkinter, the GUI provides:
Train Data: Trains the decision tree model with selected seed values.
Test Data: Evaluates the model, displaying accuracy and confusion matrix.
Make Prediction: Accepts input (age, gender, month, year, encounter type) and predicts the bear type.
Interactive interface with validation for inputs (e.g., gender, encounter type).
Decision Tree (MyDecisionTreeBear.py):

Implements a Decision Tree Classifier using scikit-learn.

Key functionalities:
Preprocessing data with one-hot encoding and handling missing values.
Training the model with a user-specified seed for reproducibility.
Testing the model and calculating metrics (accuracy, confusion matrix).
Making predictions based on new input data.
Dataset (data (3).csv):

Contains historical bear encounter data with fields like age, gender, month, year, and encounter type.
Target variable: "Type of bear."
Technologies Used
Python: Programming language.
Tkinter: For GUI development.
Scikit-learn: For machine learning (decision tree classifier).
Pandas: For data manipulation.
NumPy: For numerical operations.


Usage:

Train the model by selecting a seed value and clicking "Train Data."
Test the model to view its accuracy and confusion matrix.
Enter encounter details to predict the type of bear.

Key Features
Interactive GUI:
Simplifies model training, testing, and predictions.
Customizable Model:
Select seed values for reproducible experiments.
Accurate Predictions:
Decision tree model trained on real-world data.
