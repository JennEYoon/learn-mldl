from builtins import range
import numpy as np
from random import shuffle
#from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # DONE: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    num_samples = X.shape[0]        # for N
    num_classes = W.shape[1]        # for C
    num_pixel = X.shape[1]          # for D

    for i in range(num_samples):
        # reset to 0.0, where f as vector of scores
        f = np.zeros(num_classes)
        f_sum = 0.0

        f = X[i].dot(W)
        # applying numerical stability
        f -= np.max(f)          
        sum_f = np.sum(np.exp(f))
        
        loss += -f[y[i]] + np.log(sum_f)

        # calculate gradient, -X[y[i]] + X[i]*exp(f) / sum_f
        gradient = np.zeros((num_pixel,num_classes), dtype=float)
        for j in range(num_pixel):
            for k in range(num_classes):
                gradient[j,k] += X[i,j] * (np.exp(f[k] / sum_f)) 
        dW += gradient / sum_f

        # adjust for the true outcome y[i]
        dW[:,y[i]] -= X[i]


    loss /= num_samples
    dW /= num_samples

    # perform regularization
    loss += 0.5 * reg * (np.sum((W.reshape(num_classes, num_pixel)).dot(W), axis=1))[0]
    dW += reg * W
    #pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # DONE: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    num_samples = X.shape[0]        # for N
    num_classes = W.shape[1]        # for C   
    num_pixel = X.shape[1]          # for D
    # calculating vector of scores
    f = np.zeros(num_classes)

    f = X.dot(W)
    f -= (np.max(f, axis=1)).reshape(-1,1)      # applying numerical stability

    sum_f = (np.sum(np.exp(f), axis=1)).reshape(-1,1)

    loss = np.sum((-f[y] + np.log(sum_f)), axis=0) / num_samples

    dW = ((X.reshape(num_pixel, num_samples)).dot(np.exp(f) / sum_f)) / num_samples

    # perform regularization
    loss += 0.5 * reg * (np.sum((W.reshape(num_classes, num_pixel)).dot(W), axis=1))[0]
    dW += reg * W
    #pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
