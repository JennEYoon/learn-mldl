from pybrain.datasets import SupervisedDataSet

# handling datasets

data = SupervisedDataSet(2,1)

data.addSample((0,0),(0))
data.addSample((1,0),(1))
data.addSample((0,1),(1))
data.addSample((1,1),(0))

print(len(data))

for inp, targ in data:
	print("Input: ", inp, " output: ", targ)
	
print(data['input'])
print(data['target'])


