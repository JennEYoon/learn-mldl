import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import preprocessing

creditData = pd.read_csv("C:\\Users\\User\\Desktop\\credit_data.csv")

# Logistic regression accuracy: 93%
# we do better with knn: 97.5% !!!!!!!!
# 84%

#print(creditData.head())
#print(creditData.describe())
#print(creditData.corr())

features = creditData[["income","age","loan"]]
targetVariables = creditData.default

features = preprocessing.MinMaxScaler().fit_transform(features) #HUGE DIFFERENCE !!!

featureTrain, featureTest, targetTrain, targetTest = train_test_split(features,targetVariables, test_size=0.3)

model = KNeighborsClassifier(n_neighbors=4)  # k value !!!
fittedModel = model.fit(featureTrain, targetTrain)
predictions = fittedModel.predict(featureTest)

print(confusion_matrix(targetTest, predictions))
print(accuracy_score(targetTest,predictions))