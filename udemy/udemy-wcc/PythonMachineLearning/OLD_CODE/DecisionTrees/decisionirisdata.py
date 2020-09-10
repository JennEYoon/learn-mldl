import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


irisData = pd.read_csv("C:\\Users\\User\\Desktop\\iris_data.csv")

#print(irisData.head)
features = irisData[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
targetVariables = irisData.Class 

featureTrain, featureTest, targetTrain, targetTest = train_test_split(features, targetVariables, test_size=.2)

model = DecisionTreeClassifier()
fittedModel = model.fit(featureTrain, targetTrain)
predictions = fittedModel.predict(featureTest)

print(confusion_matrix(targetTest, predictions))
print(accuracy_score(targetTest, predictions))
