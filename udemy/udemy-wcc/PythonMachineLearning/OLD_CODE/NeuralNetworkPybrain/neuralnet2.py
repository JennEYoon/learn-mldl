from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer, BiasUnit
from pybrain.structure import FullConnection

network = FeedForwardNetwork()

inputLayer = LinearLayer(2)
hiddenLayer = SigmoidLayer(3)
outputLayer = SigmoidLayer(1)

bias1 = BiasUnit()
bias2 = BiasUnit()

network.addModule(bias1)
network.addModule(bias2)

network.addInputModule(inputLayer)
network.addModule(hiddenLayer)
network.addOutputModule(outputLayer)

inputHidden = FullConnection(inputLayer, hiddenLayer)
hiddenOutput = FullConnection(hiddenLayer, outputLayer)

biasToHidden = FullConnection(bias1, hiddenLayer)
biasToOutput = FullConnection(bias2, outputLayer)

network.addConnection(inputHidden)
network.addConnection(hiddenOutput)

network.addConnection(biasToHidden)
network.addConnection(biasToOutput)

#initialize layers + modules are sorted topologically
network.sortModules()

print(network)
print(biasToHidden.params)
print(biasToOutput.params)