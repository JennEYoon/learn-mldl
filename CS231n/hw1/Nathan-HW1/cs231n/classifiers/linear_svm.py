from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange

#############################################################################
def svm_loss_naive(W, X, y, reg):
    """
    Structured SVM loss function, naive implementation (with loops).

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
    dW = np.zeros(W.shape) # initialize the gradient as zero

    # Compute the loss and the gradient:
    num_classes = W.shape[1]
    num_train = X.shape[0]
    loss = 0.0
    for i in range(num_train):
        scores = X[i].dot(W)
        correct_class_score = scores[y[i]]
        for j in range(num_classes):
            if j == y[i]:
                continue
            margin = scores[j] - correct_class_score + 1 # note delta = 1

            if margin > 0:
                loss += margin

    #############################################################################
              # My additions to the cs231n code:
      # -nxb,  Sun Jun 23 21:46:57 EDT 2019   (Nathan X. Bendich)
    #############################################################################
                # Take gradient:
                # X[i] is the gradient  because it's a partial derivative w.r.t. W[:,y[i]].

                ###################################################################################################
                # TODO: rename all the mysterious, cryptic abstract variables so you can better wrap your head around everything
                #  especially if you come back to it in about ~1 month.    -nxb ("Nathan X. Bendich") (Tue Jun 25 20:13:58 EDT 2019)
                ###################################################################################################
                # - Correct label
                dW[:,y[i]]  -=  X[i]
                # + incorrect label
                dW[:,j]     +=  X[i]
    # end loop "for i in range(num_train):"

    #############################################################################
    # Right now the gradient is a sum over all training examples, but we want it
    # to be an average instead. so we divide by num_train.
    dW  /=  num_train
    #############################################################################

    # Right now the loss is a sum over all training examples, but we want it
    # to be an average instead. so we divide by num_train.
    loss  /=  num_train

    # Add regularization to the loss.
    loss += reg * np.sum(W * W)

    #############################################################################
    # TODO:                                                                     #
    # Compute the gradient of the loss function and store it dW.                #
    # Rather that first computing the loss and then computing the derivative,   #
    # it may be simpler to compute the derivative at the same time that the     #
    # loss is being computed. As a result you may need to modify some of the    #
    # code above to compute the gradient.                                       #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****


    #############################################################################
    # Partial derivative of d(reg_term) / dW   == 2*lambda*W

    # It's easier to see if we do it elementwise; the regularization term   is reg*(element**2).  
    #   So    d(term) / d(element)  == 2*reg*element
    dW += 2*reg*W
    #############################################################################
    # -nxb,  Sun Jun 23 21:46:57 EDT 2019   (Nathan X. Bendich)


    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
 
    return loss, dW
#############################################################################
# end function    "svm_loss_naive(W, X, y, reg):"
#############################################################################
#############################################################################



#############################################################################
def svm_loss_vectorized(W, X, y, reg):
    """
    Structured SVM loss function, vectorized implementation.

    Inputs and outputs are the same as svm_loss_naive.
    """
    #############################################################################
    # NOTE: could be improved && simplified using code found in slides at http://cs231n.stanford.edu/slides/2019/cs231n_2019_lecture03.pdf  
    # the keyword to search for is "def L_i_vectorized(x, y, W):"  .
    # -nxb,  Sun Jun 23 21:46:57 EDT 2019   (Nathan X. Bendich)
    #############################################################################
    loss = 0.0
    dW = np.zeros(W.shape) # initialize the gradient as zero

    #############################################################################
    # TODO:                                                                     #
    # Implement a vectorized version of the structured SVM loss, storing the    #
    # result in loss.                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    # TODO: comments    (brief explanation)

    # If you have questions, please see the function "svm_loss_naive()" :
    #   Most of the code implemented there is the same as the code implemented here, although with 2 for loops instead of vectorization
    # -nxb (Sun Jun 23 21:46:57 EDT 2019)   (Nathan X. Bendich)
    n_classes = W.shape[1]
    n_train = X.shape[0]

    # Vectorized version of "scores = X[i].dot(W)" from "...naive()"
    scores=X.dot(W) # scores.shape==(N, 10)

    #############################################################################
    # -nxb,  Sun Jun 23 21:46:57 EDT 2019   (Nathan X. Bendich)

    # Vectorized version of " correct_class_score = scores[y[i]]" from "svm_loss_naive()"
    # corrects_scores.shape == (n_train,)    so in the line after this we reshape:
    corrects_scores = scores[range(n_train), y]

    # Reshape "corrects" to (n_train, n_classes)      
    # I did this so we can subtract the loss in the next line in a vectorized way
    corrects_scores = np.repeat(
      corrects_scores.reshape( n_train, 1 ),
      n_classes,
      axis=1)

    # Vectorized version of "margin = scores[j] - correct_class_score + 1" from "...naive()"
    margins = scores - corrects_scores + 1 # NOTE: here, our delta == 1

    # We only want to change the loss and grads "dW" if margin > 0 
    # Vectorized version of "if margin > 0: ..." from "...naive()"
    # See "svm_loss_naive()" for full explanation;   "loss+=margin; dW[...]+=... and dW[...]-=..."
    margins[np.less(margins, 0)] = 0

    # We added too many "1"s when we failed to account for the "if j==y[i]: continue" from the naive implementation  "svm_loss_naive(W, X, y, reg)"
    # Vectorized version of "if j==y[i]: continue" from "...naive()"
    margins[range(margins.shape[0]),y]=0

    # We want the loss to be an average instead so we divide by num_train.
    loss    =  np.sum(margins)    / n_train

    # Add regularization to the loss.
    loss  += reg * np.sum(W * W)


    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****





    #############################################################################
    # TODO:                                                                     #
    # Implement a vectorized version of the gradient for the structured SVM     #
    # loss, storing the result in dW.                                           #
    #                                                                           #
    # Hint: Instead of computing the gradient from scratch, it may be easier    #
    # to reuse some of the intermediate values that you used to compute the     #
    # loss.                                                                     #
    #############################################################################


    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    #######################################
    # "On" locations from "margins" (ie. where margins > 0 from "...naive()"  )
    ons=np.greater(margins, 0).astype('int64') # 'int64' b/c zeros and ones are more intuitive for matrix multiplication than bools

    # Vectorized version of "dW[:,j] += X[i]" from "...naive()"
    dW  += ((ons.T).dot(X)).T

    # Vectorized version of "dW[:,y[i]] += X[i]" from "...naive()"
    ACROSS=1
    # ons2 just helps you select the right indices && the right # of multiples of the X[i] values.
    # ie. {start vector:    ([2*x[0], 3*x[1],  0*x[2], ..., 9*x[n_train]] ...)
    ons2= np.zeros(ons.shape)
    ons2[ range(y.shape[0]), y]     = np.sum(ons, axis=ACROSS)
    dW  -= (    (ons2.T).dot(X)    ).T

    #######################################
    # Right now the gradient is a sum over all training examples, but we want it
    # to be an average instead. so we divide by num_train.
    dW  /=  n_train
    #######################################

    #######################################
    # Derivative w.r.t. W of loss due to regularization:
    dW  += 2*reg*W
    #######################################
    # -nxb,  Sun Jun 23 21:46:57 EDT 2019   (Nathan X. Bendich)

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****



    return loss, dW
#############################################################################



















