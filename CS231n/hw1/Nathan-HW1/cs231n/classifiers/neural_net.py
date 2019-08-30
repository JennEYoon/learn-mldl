from __future__ import print_function

from builtins import range
from builtins import object
import numpy as np
import matplotlib.pyplot as plt
from past.builtins import xrange

from copy import deepcopy
from collections import OrderedDict

#===================================================================================================
class TwoLayerNet(object):
    """
    A two-layer fully-connected neural network. The net has an input dimension of
    N, a hidden layer dimension of H, and performs classification over C classes.
    We train the network with a softmax loss function and L2 regularization on the
    weight matrices. The network uses a ReLU nonlinearity after the first fully
    connected layer.

    In other words, the network has the following architecture:

    input - fully connected layer - ReLU - fully connected layer - softmax

    The outputs of the second fully-connected layer are the scores for each class.
    """

#===================================================================================================
    def __init__(self, input_size, hidden_size, output_size, std=1e-4):
        """
        Initialize the model. Weights are initialized to small random values and
        biases are initialized to zero. Weights and biases are stored in the
        variable self.params, which is a dictionary with the following keys:

        W1: First layer weights; has shape (D, H)
        b1: First layer biases; has shape (H,)
        W2: Second layer weights; has shape (H, C)
        b2: Second layer biases; has shape (C,)

        Inputs:
        - input_size: The dimension D of the input data.
        - hidden_size: The number of neurons H in the hidden layer.
        - output_size: The number of classes C.
        """

        # Save initialization parameters:
        self.nn_architecture={
          'input_size':   input_size,
          'hidden_size':  hidden_size,
          'output_size':  output_size,
        }

        self.params = {}
        self.params['W1'] = std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)
        self.params['initial_W1'] = deepcopy(self.params['W1'])
        self.params['initial_b1'] = deepcopy(self.params['b1'])
        self.params['initial_W2'] = deepcopy(self.params['W2'])
        self.params['initial_b2'] = deepcopy(self.params['b2'])
#===================================================================================================
#  end func def of 
#    __init__(self, input_size, hidden_size, output_size, std=1e-4):
#===================================================================================================


#===================================================================================================
    def loss(self, X, y=None, reg=0.0):
#===================================================================================================
        """
        Compute the loss and gradients for a two layer fully connected neural
        network.

        Inputs:
        - X: Input data of shape (N, D). Each X[i] is a training sample.
        - y: Vector of training labels. y[i] is the label for X[i], and each y[i] is
          an integer in the range 0 <= y[i] < C. This parameter is optional; if it
          is not passed then we only return scores, and if it is passed then we
          instead return the loss and gradients.
        - reg: Regularization strength.

        Returns:
        If y is None, return a matrix scores of shape (N, C) where scores[i, c] is
        the score for class c on input X[i].

        If y is not None, instead return a tuple of:
        - loss: Loss (data loss and regularization loss) for this batch of training
          samples.
        - grads: Dictionary mapping parameter names to gradients of those parameters
          with respect to the loss function; has the same keys as self.params.
        """
        # Unpack variables from the params dictionary
        W1, b1 = self.params['W1'], self.params['b1']
        W2, b2 = self.params['W2'], self.params['b2']
        N, D = X.shape
        H, C = W2.shape

        # Compute the forward pass
        scores = None
        #############################################################################   in func "loss"
        # TODO: Perform the forward pass, computing the class scores for the input. #
        # Store the result in the scores variable, which should be an array of      #
        # shape (N, C).                                                             #
        #############################################################################   in func "loss"
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        # I heavily borrowed from [Karpathy](http://cs231n.github.io/neural-networks-case-study/)      
        # -nxb,  Tue Jul  2 18:16:27 EDT 2019    (Nathan X. Bendich)
        """
        # TODO: leaky ReLU.  But have to update the gradient(s)
        linear_output=X.dot(W1)+b1
        hidden_layer= np.maximum(0.01 *linear_output , linear_output) # this line's "np.maximum()" is ReLU..
        """
        hidden_layer= np.maximum(0, X.dot(W1)   + b1) # this line's "np.maximum()" is ReLU..
        scores      = hidden_layer.dot(W2)  + b2
        assert (scores.shape == (N, C)) 
        # would have been (500, 10) in SVM for CIFAR-10 in cs231n assn1 -nxb,     Tuesday, July 2, 2019   18:16:27 EDT

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        # If the targets are not given, then jump out, we're done
        if y is None:
            return scores
        # Compute the loss
        loss = None
        #############################################################################
        # TODO: Finish the forward pass, and compute the loss. This should include  #
        # both the data loss and L2 regularization for W1 and W2. Store the result  #
        # in the variable loss, which should be a scalar. Use the Softmax           #   in func "loss"
        # classifier loss.                                                          #
        #############################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        ACROSS=1
        # The Gradient fix I do on the line below  is from the inimitable [Eli Bendersky](https://eli.thegreenplace.net/2016/the-softmax-function-and-its-derivative/ )
        # (scores.T).shape ==  (C,N)
        # np.max(scores,axis=ACROSS).shape ==  (N,)
        scores=(scores.T -\
                np.max(scores,axis=ACROSS)
                ).T
        # Softmax   (compute class probabilities):
        exp_scores  = np.exp(scores)      # exp_scores.shape == (200,3) or (5,3)   (N,C)
        probs       = exp_scores/np.sum(exp_scores, axis=1, keepdims=True)

        # Loss:
        correct_logprobs = -np.log(probs[range(N),y])
        data_loss = np.sum(correct_logprobs)/N
        reg_loss = 0.5*reg*   ( np.sum(W1*W1)   +   np.sum(W2*W2) )
        loss = data_loss + reg_loss
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        # Backward pass: compute gradients
        grads = {}
        #############################################################################
        # TODO: Compute the backward pass, computing the derivatives of the weights #
        # and biases. Store the results in the grads dictionary. For example,       #
        # grads['W1'] should store the gradient on W1, and be a matrix of same size #
        #############################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        dscores = probs
        dscores[range(N), y] -= 1
        dscores/= N

        # backprop through hidden layer:
        dW2 = (hidden_layer.T)  .dot(dscores)

        # W2 and b2   (partial derivatives, or more technically, the [Jacobian](https://eli.thegreenplace.net/2016/the-softmax-function-and-its-derivative/)).
        db2 = np.sum(dscores, axis=0, keepdims=True)
        dhidden = dscores.dot( W2.T)
        # backprop through the ReLU non-linearity
        dhidden[hidden_layer <= 0] = 0

        # W1, b1
        dW1 = (X.T).dot(dhidden)
        db1 = np.sum(dhidden, axis=0, keepdims=True)

        # Return gradients:
        grads['W2'] = dW2       + reg*W2
        grads['b2'] = db2       + reg*b2
        grads['W1'] = dW1       + reg*W1
        grads['b1'] = db1       + reg*b1
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        return loss, grads

        # why is this slower for bigger minibatches than for smaller ones?  Isn't everything parallelized?
#===================================================================================================
# end func def of "loss(self, X, y=None, reg=0.0):"
#===================================================================================================



#===================================================================================================
    def train(self, X, y, X_val, y_val,
              learning_rate=1e-3, learning_rate_decay=0.95,
              reg=5e-6, num_iters=100,
              batch_size=200, verbose=False):
    #===================================================================================================
        """
        Train this neural network using stochastic gradient descent.

        Inputs:
        - X: A numpy array of shape (N, D) giving training data.
        - y: A numpy array f shape (N,) giving training labels; y[i] = c means that
          X[i] has label c, where 0 <= c < C.
        - X_val: A numpy array of shape (N_val, D) giving validation data.
        - y_val: A numpy array of shape (N_val,) giving validation labels.
        - learning_rate: Scalar giving learning rate for optimization.
        - learning_rate_decay: Scalar giving factor used to decay the learning rate
          after each epoch.
        - reg: Scalar giving regularization strength.
        - num_iters: Number of steps to take when optimizing.
        - batch_size: Number of training examples to use per step.
        - verbose: boolean; if true print progress during optimization.
        """
        num_train = X.shape[0]
        iterations_per_epoch = max(num_train / batch_size, 1)  # max((num_train / batch_size)  / 100, 1)   # I added the 100  as an experiment to see if I could get the val_acc at every iteration   WITHOUT losing too much speed    -nxb 
        self.hyperparams=OrderedDict()
        self.hyperparams["learning_rate"]       =     learning_rate       
        self.hyperparams["reg"]       =     reg       
        self.hyperparams["H"]       =     self.nn_architecture['hidden_size']
        self.hyperparams["num_iters"]       =     num_iters       
        self.hyperparams["batch_size"]       =     batch_size       

        # Use SGD to optimize the parameters in self.model
        loss_history = []
        train_acc_history = []
        val_acc_history = []

        for it in range(num_iters):
            X_batch = None
            y_batch = None

            #########################################################################
            # TODO: Create a random minibatch of training data and labels, storing  #
            # them in X_batch and y_batch respectively.                             #
            #########################################################################
            # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
            img_indices=np.random.choice(num_train, batch_size)
            X_batch = X[img_indices]      # "batch_size" many training images   X_batch.shape==(200, 3072)
            y_batch = y[img_indices]
            # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

            # Compute loss and gradients using the current minibatch
            loss, grads = self.loss(X_batch, y=y_batch, reg=reg)
            loss_history.append(loss)

            #########################################################################
            # TODO: Use the gradients in the grads dictionary to update the         #
            # parameters of the network (stored in the dictionary self.params)      #
            # using stochastic gradient descent. You'll need to use the gradients   #
            # stored in the grads dictionary defined above.                         #
            #########################################################################
            # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

            # ie. grads['b1'].shape == (1, 10)
            if grads['b1'].shape[0] == 1: db1 = grads['b1'].reshape((grads['b1'].shape[1],))
            else:                         db1 = grads['b1']

            # ie. grads['b2'].shape == (1, 3)
            if grads['b2'].shape[0] == 1: db2 = grads['b2'].reshape((grads['b2'].shape[1],))
            else:                         db2 = grads['b2']

            self.params['W1'] -= (grads['W1'] *learning_rate)
            self.params['W2'] -= (grads['W2'] *learning_rate)
            self.params['b1'] -= ( db1        *learning_rate)
            self.params['b2'] -= ( db2        *learning_rate)

            # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

            if verbose and it % 100 == 0:
                print('iteration %d / %d: loss %f' % (it, num_iters, loss))

            # Every epoch, check train and val accuracy and decay learning rate.
            if it % iterations_per_epoch == 0:
                # Check accuracy
                train_acc = (self.predict(X_batch) == y_batch).mean()
                val_acc = (self.predict(X_val) == y_val).mean()
                train_acc_history.append(train_acc)
                val_acc_history.append(val_acc)

                # Decay learning rate
                learning_rate *= learning_rate_decay
                #  Dammit.  I decayed the lr tooo fast when I made "iterations_per_epoch" much much smaller.

        return {
          'loss_history': loss_history,
          'train_acc_history': train_acc_history,
          'val_acc_history': val_acc_history,
        }
###########################################################################
#   # end func def of:
#       train(self, X, y, X_val, y_val,
#             learning_rate=1e-3, learning_rate_decay=0.95,
#             reg=5e-6, num_iters=100,
#             batch_size=200, verbose=False):
###########################################################################










###########################################################################
    def predict(self, X):
        """
        Use the trained weights of this two-layer network to predict labels for
        data points. For each data point we predict scores for each of the C
        classes, and assign each data point to the class with the highest score.

        Inputs:
        - X: A numpy array of shape (N, D) giving N D-dimensional data points to
          classify.

        Returns:
        - y_pred: A numpy array of shape (N,) giving predicted labels for each of
          the elements of X. For all i, y_pred[i] = c means that X[i] is predicted
          to have class c, where 0 <= c < C.
        """
        y_pred = None

        ###########################################################################
        # TODO: Implement this function; it should be VERY simple!                #
        ###########################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        ACROSS=1
        scores = self.loss(X, y=None, reg=5e-6) # if y=None, returns scores instead of tuple of (loss, grads)
        y_pred = np.argmax(scores, axis=ACROSS)
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        return y_pred
###########################################################################
###########################################################################
#   # end func def of:
#       predict(self, X):
###########################################################################
