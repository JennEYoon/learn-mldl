from __future__ import print_function

from builtins import range
from builtins import object
import numpy as np
from cs231n.classifiers.linear_svm import *
from cs231n.classifiers.softmax import *
from past.builtins import xrange

from collections import OrderedDict
from copy import deepcopy


###########################################################################
class LinearClassifier(object):

###########################################################################
    def __init__(self):
        self.W = None
        self.params=OrderedDict()
        self.params['init_W']=deepcopy(self.W)
        self.params['W']=self.W

###########################################################################
    def train(self, X, y, learning_rate=1e-3, reg=1e-5, num_iters=100,
              batch_size=200, verbose=False):
        """
        Train this linear classifier using stochastic gradient descent.

        Inputs:
        - X: A numpy array of shape (N, D) containing training data; there are N
          training samples each of dimension D.
        - y: A numpy array of shape (N,) containing training labels; y[i] = c
          means that X[i] has label 0 <= c < C for C classes.
        - learning_rate: (float) learning rate for optimization.
        - reg: (float) regularization strength.
        - num_iters: (integer) number of steps to take when optimizing
        - batch_size: (integer) number of training examples to use at each step.
        - verbose: (boolean) If true, print progress during optimization.

        Outputs:
        A list containing the value of the loss function at each training iteration.
        """
        num_train, dim = X.shape
        num_classes = np.max(y) + 1 # assume y takes values 0...K-1 where K is number of classes
        if self.W is None:
            # lazily initialize W
            self.W = 0.001 * np.random.randn(dim, num_classes)
            self.params['init_W']=deepcopy(self.W)
            self.params['W']=self.W

        # Run stochastic gradient descent to optimize W
        loss_history = []
        for it in range(num_iters):
            X_batch = None
            y_batch = None

            #########################################################################
            # TODO:                                                                 #
            # Sample batch_size elements from the training data and their           #
            # corresponding labels to use in this round of gradient descent.        #
            # Store the data in X_batch and their corresponding labels in           #
            # y_batch; after sampling X_batch should have shape (batch_size, dim)   #
            # and y_batch should have shape (batch_size,)                           #
            #                                                                       #
            # Hint: Use np.random.choice to generate indices. Sampling with         #
            # replacement is faster than sampling without replacement.              #
            #########################################################################
            # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

            # "minibatch"
            # -nxb,  Sun Jun 23 21:46:57 EDT 2019   (Nathan X. Bendich)
            img_indices=np.random.choice(num_train, batch_size)
            X_batch = X[img_indices]      # "batch_size" many training images   X_batch.shape==(200, 3072)
            y_batch = y[img_indices]

            # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

            # Evaluate loss and gradient:
            loss, grad = self.loss(X_batch, y_batch, reg)
            loss_history.append(loss)

            #########################################################################
            # TODO:                                                                 #
            # Update the weights using the gradient and the learning rate.          #
            #########################################################################
            # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

            # Update gradients:
            # Gradients point upward (ie. "Where I should step if I want to RAISE the value of the loss func?")
            # So I do gradient DESCENT and do self.W MINUS-equals  ("self.W-=grad*learning_rate")
            # -nxb,  Sun Jun 23 21:46:57 EDT 2019   (Nathan X. Bendich)
            self.W -= (grad*learning_rate) 
            self.params['W']=self.W

            # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

            if verbose and it % 100 == 0:
                print('iteration %d / %d: loss %f' % (it, num_iters, loss))

        return loss_history
###########################################################################

###########################################################################
    def predict(self, X):
        """
        Use the trained weights of this linear classifier to predict labels for
        data points.

        Inputs:
        - X: A numpy array of shape (N, D) containing training data; there are N
          training samples each of dimension D.

        Returns:
        - y_pred: Predicted labels for the data in X. y_pred is a 1-dimensional
          array of length N, and each element is an integer giving the predicted
          class.
        """
        y_pred = np.zeros(X.shape[0])
        ###########################################################################
        # TODO:                                                                   #
        # Implement this method. Store the predicted labels in y_pred.            #
        ###########################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        # NOTE to self:
        # NOTE to self:   I almost certainly could have used previously-implemented-code to make this method shorter & more code reuse (always a good thing) -nxb, date == "Tue Jul  2 18:01:45 EDT 2019"
        # NOTE to self:

        # self.W.shape == (3073, 10)            
        # X.shape == (49000, 3073)
        all_scores= X.dot(self.W)
        ACROSS=1
        # Return the highest score output from softmax for each image.
        # This is the prediction (which class the SVM thinks the image belongs to)
        y_pred  = np.argmax(all_scores, axis=ACROSS)

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        return y_pred
###########################################################################
#   end function definition predict(self, X)
###########################################################################

###########################################################################
    def loss(self, X_batch, y_batch, reg):
        """
        Compute the loss function and its derivative.
        Subclasses will override this.

        Inputs:
        - X_batch: A numpy array of shape (N, D) containing a minibatch of N
          data points; each point has dimension D.
        - y_batch: A numpy array of shape (N,) containing labels for the minibatch.
        - reg: (float) regularization strength.

        Returns: A tuple containing:
        - loss as a single float
        - gradient with respect to self.W; an array of the same shape as W
        """
        pass
###########################################################################


###########################################################################
class LinearSVM(LinearClassifier):
    """ A subclass that uses the Multiclass SVM loss function """

    def loss(self, X_batch, y_batch, reg):
        return svm_loss_vectorized(self.W, X_batch, y_batch, reg)


###########################################################################
class Softmax(LinearClassifier):
    """ A subclass that uses the Softmax + Cross-entropy loss function """

    def loss(self, X_batch, y_batch, reg):
        #return softmax_loss_naive(self.W, X_batch, y_batch, reg)
        return softmax_loss_vectorized(self.W, X_batch, y_batch, reg)


###########################################################################




















































