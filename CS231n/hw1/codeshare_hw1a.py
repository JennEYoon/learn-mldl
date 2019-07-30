"""
This is a shared scratch pad for homework 1 discussion.
Paste your code here to ask help.  Copy from here to your 
computer to RUN python code.  You can edit directly here too.
May 27, 2019 Monday 7pm start remote discussion.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# For Jupyter notebook, keep line below.
%matplotlib inline  



        test_sum = np.sum(np.square(X), axis=1)[:, np.newaxis] # need to re-format
        train_sum = np.sum(np.square(self.X_train), axis=1)
        x_y = np.dot(X, self.X_train.T)
        dists = np.sqrt(test_sum + train_sum - 2*x_y)
        
#Using Counter from collections        
def most_frequent(list):
    counted = Counter(list)
    return counted.most_common(1)[0][0]
    
    ########################################################
    
            num_test = dists.shape[0]
        y_pred = np.zeros(num_test)
        for i in range(num_test):
            # A list of length k storing the labels of the k nearest neighbors to
            # the ith test point.
            closest_y = []
            #########################################################################
            # TODO:                                                                 #
            # Use the distance matrix to find the k nearest neighbors of the ith    #
            # testing point, and use self.y_train to find the labels of these       #
            # neighbors. Store these labels in closest_y.                           #
            # Hint: Look up the function numpy.argsort.                             #
            #########################################################################
            # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
            
            # We are looking for the k columns that have the smallest distances for row i
            ourRow = dists[i]

            bestIndices = np.argsort( ourRow )
            
            myList = np.zeros( k )
            for idx in range(k):
                myList[idx] = self.y_train[bestIndices[idx]]
    
    y_pred[i] = Counter(myList).most_common(1)[0][0]
    
    ########################################################
    
    ***np.bincount()***
    https://docs.scipy.org/doc/numpy/reference/generated/numpy.bincount.html

#Using np.unique
labels, counts = np.unique(closest_y,return_counts = True)
            sorted_labels = labels[np.argsort(counts)]
            y_pred[i] = sorted_labels[-1]
            
            
            
            
            
            http://cs231n.github.io/linear-classify/
            
          
	GUTS of svm_loss_naive:

	#dW = np.zeros(W.shape) # initialize the gradient as zero
    dW = 2.0 * reg * W # initialize the gradient to the derivative of the reg. term

    # compute the loss and the gradient
    num_classes = W.shape[1] # = C
        # W11 W12 ... W1C
        # W21 W22 ... W2C
        # ...
        # WD1 WD2 ... WDC
    num_train = X.shape[0] # = N
    loss = 0.0
    for i in range(num_train):
        scores = X[i].dot(W) #linear score rule - X[i] has dim 1 by D
                             # mult 1 by D times D by C matrix
                             # result is 1 by C (This is really a long row result)
                # = scores col 1: W11 * Xi1 + W21 * Xi2 + ..... + Wd1 * Xid
                #   scores col 2: W12 * Xi1 + W22 * Xi2 + .... +  Wd2 * Xid
                # ...
                #   scores col d: [W1c * Xi1 + W2c * Xi2 + ... + Wdc * Xid
        correct_class_score = scores[y[i]] # score for correct class y[i]
                                           # wish this were largest score
        for j in range(num_classes):
            if j == y[i]:
                continue
            margin = scores[j] - correct_class_score + 1 # note delta = 1
            if margin > 0:    # We don't penalize for negative because already good then
                loss += margin/num_train
                # if we're in column/class j then the non-const part of loss is
                # margin = const + scores[j]/num_train 
                #    = ( W1j * Xi1 + W2j * Xi2 + ... + Wdj * Xid )/num_train
                # so the choice of j does not make a difference since only the
                # weight is different in column j
#                 for k in range(X.shape[1]):
#                     dW[k,j] += X[i,k]/num_train  
                    
                # help from Alexej
                dW[:,j] += X[i,:]/num_train
                # OH - I missed the derivative of the CORRECT class score GOT IT!!!
                dW[:,y[i]] -= X[i,:]/num_train 

# Right now the loss is a sum over all training examples, but we want it
# to be an average instead so we divide by num_train.
# loss /= num_train (moved up)

# Add regularization to the loss. This doesn't need to happen for all i
#     for j in range(num_classes):
#         for k in range(X.shape[1]):
#             dW[k,j] += 2*reg*W[k,j]

			loss += reg * np.sum(W * W) 