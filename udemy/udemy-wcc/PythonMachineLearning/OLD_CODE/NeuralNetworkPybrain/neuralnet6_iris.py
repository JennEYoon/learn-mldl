from pybrain.datasets import ClassificationDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer
from pylab import ion, ioff, figure, draw, contourf, clf, show, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from random import normalvariate
import numpy as np
from sklearn import datasets
import numpy.random as random

# ---------------------------------------------------------------------
#
# Iris dataset

def splitWithProportion(self, proportion = 0.7):
        """Produce two new datasets, the first one containing the fraction given
        by `proportion` of the samples."""
        indicies = random.permutation(len(self))
        separator = int(len(self) * proportion)

        leftIndicies = indicies[:separator]
        rightIndicies = indicies[separator:]

        leftDs = ClassificationDataSet(inp=self['input'][leftIndicies].copy(),
                                   target=self['target'][leftIndicies].copy())
        rightDs = ClassificationDataSet(inp=self['input'][rightIndicies].copy(),
                                    target=self['target'][rightIndicies].copy())
        return leftDs, rightDs

irisData = datasets.load_iris()
dataFeatures = irisData.data
dataTargets = irisData.target

#plt.matshow(irisData.images[11], cmap=cm.Greys_r)
#plt.show()
#print dataTargets[11]
#print dataFeatures.shape

dataSet = ClassificationDataSet(4, 1 , nb_classes=3)

for i in range(len(dataFeatures)):
	dataSet.addSample(np.ravel(dataFeatures[i]), dataTargets[i])
	
trainingData, testData = splitWithProportion(dataSet,0.7)

trainingData._convertToOneOfMany()
testData._convertToOneOfMany()

neuralNetwork = buildNetwork(trainingData.indim, 7, trainingData.outdim, outclass=SoftmaxLayer) 
trainer = BackpropTrainer(neuralNetwork, dataset=trainingData, momentum=0.01, learningrate=0.05, verbose=True)

trainer.trainEpochs(10000)
print('Error (test dataset): ' , percentError(trainer.testOnClassData(dataset=testData), testData['class']))

print('\n\n')
counter = 0
for input in dataFeatures:
	print(counter," output is according to the NN: ", neuralNetwork.activate(input))
	counter = counter + 1