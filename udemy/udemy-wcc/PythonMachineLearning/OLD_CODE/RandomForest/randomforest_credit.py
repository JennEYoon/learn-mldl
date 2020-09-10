import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# Logistic regression accuracy: 93%
# we do better with knn: 97.5% !!!!!!!!
# 84% simple kNN without normalizing the dataset
# We can achieve ~ 98.5% with random forests

creditData = pd.read_csv("C:\\Users\\User\\Desktop\\credit_data.csv")

#print(irisData.head())
#print(irisData.describe())
#print(irisData.corr())

features = creditData[["income","age","loan"]]
targetVariables = creditData.default

featureTrain, featureTest, targetTrain, targetTest = train_test_split(features, targetVariables, test_size=.2)

model = RandomForestClassifier(n_estimators=25)
fittedModel = model.fit(featureTrain, targetTrain)
predictions = fittedModel.predict(featureTest)

print(confusion_matrix(targetTest, predictions))
print(accuracy_score(targetTest, predictions))



