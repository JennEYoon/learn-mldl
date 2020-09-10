import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

creditData = pd.read_csv("C:\\Users\\User\\Desktop\\credit_data.csv")

#print(creditData.head())
#print(creditData.describe())
#print(creditData.corr())

features = creditData[["income","age","loan"]]
targetVariables = creditData.default

featureTrain, featureTest, targetTrain, targetTest = train_test_split(features,targetVariables, test_size=0.3)

model = LogisticRegression()
fittedModel = model.fit(featureTrain, targetTrain)
predictions = fittedModel.predict(featureTest)

print(confusion_matrix(targetTest, predictions))
print(accuracy_score(targetTest,predictions))