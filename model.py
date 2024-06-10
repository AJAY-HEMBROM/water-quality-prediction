import pandas as pd
import numpy as np  # Add this import statement
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle as pkle

# Load the csv file
df = pd.read_csv(r"water_potability.csv")  # Add 'r' before the string to treat it as a raw string
print(df.head())

# Select independent & dependent variable
x = df[["ph", "Hardness", "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity"]]  # Add quotes around column names
y = df["Potability"]

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=50)

# Feature Scaling
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Instantiate the model
classifier = RandomForestClassifier()

# Fit the model
classifier.fit(x_train, y_train)

# Make pickle file of our model
pkle.dump(classifier, open("model.pkl", "wb"))
