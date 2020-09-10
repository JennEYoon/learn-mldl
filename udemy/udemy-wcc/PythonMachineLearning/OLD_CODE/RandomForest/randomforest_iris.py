import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import datasets


#irisData = pd.read_csv("C:\\Users\\User\\Desktop\\iris_data.csv")
irisData = datasets.load_iris()

#print(irisData)
#print(irisData.describe())
#print(irisData.corr())

features = irisData.data
targetVariables = irisData.target

featureTrain, featureTest, targetTrain, targetTest = train_test_split(features, targetVariables, test_size=.2)

model = RandomForestClassifier(n_estimators=100)
fittedModel = model.fit(featureTrain, targetTrain)
predictions = fittedModel.predict(featureTest)

print(confusion_matrix(targetTest, predictions))
print(accuracy_score(targetTest, predictions))

