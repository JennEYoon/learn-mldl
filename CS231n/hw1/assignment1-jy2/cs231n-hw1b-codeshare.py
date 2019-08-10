"""
Homework Session June 26 2019, 7pm start -- Codeshare File Saved.
This is a shared scratch pad for our 2nd homework discussion.
Paste your code here to ask for help or to share a solution.
Copy from here to your computer to RUN python code.  
You can edit directly here too.

CodeShare.io is Google Docs for code, multi-user editable code-pad.

Thank you Andrew!!!
Thanks to everyone for participating!

Jennifer
"""

import numpy as np
import matplotlib.pyplot as plt

##################### Code Examples ######################
# softmax_loss_naive example code (Peter):

    
    num_classes = W.shape[1]
    num_samples = X.shape[0]

    for i in range(num_samples):
        # Compute vector of scores
        f = X[i].dot(W)

        # Apply numerical stability term
        # Shift values so that highest value is 0.
        f -= np.max(f)

        # Compute loss (and add it up and divided later)
        sum_i = np.sum(np.exp(f))
        loss += -f[y[i]] + np.log(sum_i)

        # Compute gradient
        for j in range(num_classes):
            dW[:, j] += np.exp(f[j])/sum_i * X[i]
        # 'Fix' the weights for the true values.
        dW[:, y[i]] -= X[i]

    # Compute average
    loss /= num_samples
    dW /= num_samples

    # Regularization
    loss += 0.5 * reg * np.sum(W * W)
    dW += reg * W
    
    
# softmax_loss_vectorized example code (Peter):

    num_samples = X.shape[0]
    # Compute vector of scores
    f = X.dot(W)
    # Apply numerical stability term
    f -= np.max(f)

    sum_exp = np.exp(f).sum(axis=1, keepdims=True)
    softmax = np.exp(f)/sum_exp
    loss = np.sum(-np.log(softmax[np.arange(num_samples), y]) )

    # Weight Gradient
    softmax[np.arange(num_samples), y] -= 1
    dW = X.T.dot(softmax)

    # Compute average
    loss /= num_samples
    dW /= num_samples

    # Regularization
    loss += 0.5 * reg * np.sum(W * W)
    dW += reg * W

    


#Gradient (Chris M)   
#correct = softmax[range(num_train),y] #The value of softmax for correct category
#correct_mask = (softmax == correct[:,np.newaxis]*np.ones(softmax.shape))
#dW = (X.T @ (softmax - correct_mask))/num_train + 2*reg*W
