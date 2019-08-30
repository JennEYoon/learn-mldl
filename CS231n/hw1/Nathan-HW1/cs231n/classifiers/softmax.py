from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange

# NOTE: the version of "naive()" used is *EXTREMELY* slow.



# Best implementations are at the END of this code, copied from https://github.com/martinkersner/cs231n/blob/master/assignment1/softmax.py   (they use Karpathy/Bendersky's derivation of the softmax Jacobian at:

  # Karpathy:
  #   http://cs231n.github.io/neural-networks-case-study/
  # Bendersky:
  #   https://eli.thegreenplace.net/2016/the-softmax-function-and-its-derivative/

 
# Simpler code that evaluates the same gradient and loss:

###################################################################################################
def vectorized_MartinKersner(W, X, y, reg):
    '''
        I lifted this code from https://github.com/martinkersner/cs231n/blob/master/assignment1/softmax.py
        Now I'm just checking whether it works.
    '''
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # Compute the softmax loss and its gradient using no explicit loops.        #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    num_train = X.shape[0]

    scores = np.dot(X, W)
    exp_scores = np.exp(scores)
    prob_scores = exp_scores/np.sum(exp_scores, axis=1, keepdims=True)
    correct_log_probs = -np.log(prob_scores[range(num_train), y])
    loss = np.sum(correct_log_probs)
    loss /= num_train
    loss += 0.5 * reg * np.sum(W**2)

    # grads
    dscores = prob_scores
    dscores[range(num_train), y] -= 1
    dW = np.dot(X.T, dscores)
    dW /= num_train
    dW += reg * W

    return loss, dW


###################################################################################################
# end func def "vectorized_MartinKersner(W, X, y, reg):"
###################################################################################################
softmax_loss_vectorized = vectorized_MartinKersner




###################################################################################################
def naive_MartinKersner(W, X, y, reg):
  # NOTE:  this function "naive_MartinKersner" is SO. SLOW.
  loss = 0.0
  dW = np.zeros_like(W)
  num_dims = W.shape[0]
  num_classes = W.shape[1]
  num_train = X.shape[0]

  for i in xrange(num_train):                         # 500 == num_train
    scores = X[i, :].dot(W)
    exp_scores = np.exp(scores)

    prob_scores = exp_scores/np.sum(exp_scores)

    for d in xrange(num_dims):                        # 3073 == num_dims == "n_pix_vals" ("n_pix_vals" is mine: (nxb's) )
        for k in xrange(num_classes):
            if k == y[i]:
                dW[d, k] += X.T[d, i] * (prob_scores[k]-1)
            else:
                dW[d, k] += X.T[d, i] * prob_scores[k]
    
    loss += -np.log(prob_scores[y[i]])

  loss /= num_train
  loss += 0.5 * reg * np.sum(W**2)
  
  dW /= num_train
  dW += reg * W

  return loss, dW
###################################################################################################
# end func def "naive_MartinKersner(W, X, y, reg):"
###################################################################################################
softmax_loss_naive = naive_MartinKersner
















































































































'''
###################################################################################################
def softmax_loss_naive(W, X, y, reg):                  # right top buffer is "naive"
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
    dW = np.zeros_like(W) # same as np.zeros(W.shape) 
    # -nxb (Nathan X. Bendich) (Mon Jun 24 13:56:08 EDT 2019)

    num_train   = n_train   = X.shape[0]
    num_classes = n_classes = dW.shape[1]
    num_pix_vals= n_pix_vals= X.shape[1]

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    # Implementation NOTES:
    # I just went straight to implementing the loss_i as a vectorized calculation.  It's faster this way, and it's easy enough with SVM loss and grad dW as a template.
    # -nxb (Nathan X. Bendich) (Mon Jun 24 13:56:08 EDT 2019)

    # Vectorized version of "scores = X[i].dot(W)" from "...naive()"
    SVM_scores=X.dot(W)         #(X.T).dot(W) # scores.shape==(N_train, 10)    ie. (500,10), for X_dev

    # unnormalized_probs.shape == (500,10)  (500==num_train)
    unnormalized_probs= raw= raw_softmax=np.exp(SVM_scores) # I also considered calling this variable "exps." 
    # -nxb (Nathan X. Bendich) (Mon Jun 24 13:56:08 EDT 2019)
  
    ACROSS=1
    # This variable "probabilities" could also called "softmax_scores"  or "softmax_outputs"
    probabilities= (unnormalized_probs.T /np.sum(unnormalized_probs, axis=ACROSS)).T  
    # probabilities.shape == (num_train, 10)    (500, 10) for X_dev

    # All comments/code written by NXB (Nathan X. Bendich)  on Monday, Jun 24 13:56:08 EDT 2019
    correct_probs=probabilities[range(num_train), y]
    # correct_probs.shape == (num_train, 10)

    ###################################################################################################
    # Calculate loss:
    ###################################################################################################
    # Sum over training images:
    tot_loss = np.sum(-np.log(correct_probs))
    # Average loss per training image
    loss = (tot_loss / num_train)
    # Regularize
    loss += np.sum(0.5*reg*W*W)

    ###################################################################################################
    # Calculate grads (dW):
    ###################################################################################################
    import math
    for i in range(num_train):
        ###################################################################################################
        # TODO: rename all the mysterious, cryptic abstract variables so you can better wrap your head around everything
        #  especially if you come back to it in about ~1 month.    -nxb ("Nathan X. Bendich") (Tue Jun 25 20:13:58 EDT 2019)
        ###################################################################################################
            # TODO: rename all the terms I've stupidly named like "dW_term_3_1," "dW_term_3_2," "dW_term_3_3," "dW_term_3_4,"

        # NOTE:  We used the "derivative quotient rule" to calculate all these strange-looking, abstract things.
        correct_class=y[i]
        dW_term_3_1 = X[i]* (math.e**(W[:, correct_class].dot(X[i]) ))
        dW_term_3_3 = np.sum (unnormalized_probs[i,:])
        dW_term_3_4 = unnormalized_probs[i, correct_class] # shape==1 (correct class' predicted score)
        #dW_term_3_2 = np.zeros(X[i].shape)
        quotient_rule_denom= dW_term_3_3 * dW_term_3_3 # squared

        for j in range(num_classes):
            # TODO: rename all the terms I've stupidly named like "dW_term_3_1," "dW_term_3_2," "dW_term_3_3," "dW_term_3_4,"
            dW_term_3_2  = X[i] * raw[i,j]

            #numerator.shape == (n_pix_val,)   # 3072 or 3073 in CIFAR-10  (the extra "+1" in 3073 comes from the bias trick)
            # TODO TODO: UNCOMMENT NEXT LINE:
            numerator =   (dW_term_3_2 * dW_term_3_4) # old version with = - ...

            # We should only raise the weights that help correctly identify the image
            if j == correct_class:
                # TODO TODO: UNCOMMENT NEXT LINE:
                numerator-= (dW_term_3_1 * dW_term_3_3)

            ########################################################################################################################################
            # TODO: uncomment     line below       (   "dW[:,j] += (numerator / quotient_rule_denom)"  )
            # TODO TODO: UNCOMMENT NEXT LINE:
            ########################################################################################################################################
            #dW[:,j] += numerator #(numerator  / quotient_rule_denom)
            dW[:,j] += (numerator / quotient_rule_denom)
            # unnormalized_probs.shape == (500,10)  (500==num_train)
            ########################################################################################################################################
        # end loop "for j in range(num_classes):"
    # end loop "for i in range(num_train):"

    # NOTE:  We used the "derivative quotient rule" to calculate all these abstract terms    that contribute to dW.

    #######################################
    # Right now the gradient is a sum over all training examples, but we want it
    # to be an average instead. so we divide by num_train.
    dW  /=  n_train
    #######################################

    #######################################
    # Partial derivative of d(reg_term) / dW   == lambda*W
    # It's easier to see if we do it elementwise; the regularization term   is 0.5*reg*(element**2).  
    #   So    d(term) / d(element)  == reg*element
    dW += reg*W
    #######################################

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
###################################################################################################

#############################################################################
def softmax_loss_vectorized(W, X, y, reg):              # right mid buffer is "1 loop" version
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
 
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W) # same as np.zeros(W.shape) 
    # -nxb (Nathan X. Bendich) (Mon Jun 24 13:56:08 EDT 2019)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    num_train   = n_train   = X.shape[0]
    num_classes = n_classes = dW.shape[1]
    num_pix_vals= n_pix_vals= X.shape[1]

    # Implementation NOTES:
    # I just went straight to implementing the loss_i as a vectorized calculation.  It's faster this way, and it's easy enough with SVM loss and grad dW as a template.
    # -nxb (Nathan X. Bendich) (Mon Jun 24 13:56:08 EDT 2019)

    # Vectorized version of "scores = X[i].dot(W)" from "...naive()"
    SVM_scores=  scores= X.dot(W)         #(X.T).dot(W) # scores.shape==(N_train, 10)    ie. (500,10), for X_dev

    # unnormalized_probs.shape == (500,10)  (500==num_train)
    unnormalized_probs=np.exp(SVM_scores) # I also considered calling this variable "exps." 
    # -nxb (Nathan X. Bendich) (Mon Jun 24 13:56:08 EDT 2019)

    DOWN=0
    ACROSS=1
    # This variable "probabilities" could also called "softmax_scores"  or "softmax_outputs"
    probabilities= (unnormalized_probs.T /np.sum(unnormalized_probs, axis=ACROSS)).T  
    # probabilities.shape == (num_train, 10)    (500, 10) for X_dev

    # All comments/code written by NXB (Nathan X. Bendich)  on Monday, Jun 24 13:56:08 EDT 2019
    correct_probs=probabilities[range(num_train), y]
    # correct_probs.shape == (num_train, 10)

    ###################################################################################################
    # Calculate loss:
    ###################################################################################################
    # Sum over training images:
    tot_loss = np.sum(-np.log(correct_probs))
    # Average loss per training image
    loss = (tot_loss / num_train)
    # Regularize
    loss += np.sum(0.5*reg*W*W)

    ###################################################################################################
    ###################################################################################################
    #
    #       Calculate gradents / "grads" / "dW"
    #
    ###################################################################################################
    ###################################################################################################
    # Below is a Fresh try  (attempt at a solution for fully_vectorized())   as of   Fri Jun 28 15:11:13 EDT 2019.

    # See uDel Evans Hall's   iSuite board (or pictures of this whiteboard)     for explanation of why I named some of these terms like "term_3_1" or "term_3_2," etc.
    #   Also may be present in my startup notes

    # I couldn't decide on the best name so I included all of them.  They're just pointers, after all.  Not wasting too much time alloc-ing memory or wasting much space by deepcopy()ing giant arrays.   -nxb,     Fri Jun 28 15:11:13 EDT 2019
    raw_softmax= exps= raw= unnormed= unnormalized_probs= unnormalized_probabilities= \
      np.exp(  X.dot(W)  )     # raw.shape == (500, 10)
    # This variable "train_2_labels" is only used to map (500 vals=>10 vals) when we need the right answers (terms labeled "corrects" below  (the 3_1 and 3_3 terms)   )
    train_2_labels = np.zeros( scores.shape ) # (500,10)
    train_2_labels[range(n_train), y]=1

    #===================================================================================================
    # "term_3_1" (AKA corrects_grad)  :
    #===================================================================================================
    # TODO: rename "scalars" something more descriptive/helpful/  , etc.
    #===================================================================================================
    scalars = np.exp(                   # scalars.shape == (500,)
      np.sum(
        W[:,y]* X.T,                    # X.T.shape == (3073, 500)
        axis=DOWN))
    # scalars.shape == (500,)
    # In the below line, corrects_grad.shape == (3073, 500)
    corrects_grad = term_3_1= (X.T* scalars)
    # (3073, 500)==corrects_grad.shape

    #===================================================================================================
    # "term_3_3" (AKA all_pre_grad) :
    #   and "denom"
    #===================================================================================================
    #   TODO: rename lots of these variables
    #===================================================================================================
    all_pre_grad = term_3_3= np.sum(raw, axis=ACROSS) # (500,)
    denom = np.repeat(
      all_pre_grad.reshape((n_train,1)),
      n_classes,
      axis=ACROSS)
      # shape == (500,10)
    denom = np.square(denom)
    all_pre_grad = (train_2_labels.T * all_pre_grad).T # all_pre_grad.shape == (500,10)

    #===================================================================================================
    # "numer8r_minus" :
    #===================================================================================================
    # The next line is  equivalent to the lines 
    #   if j == correct_class:
    #     numerator-= term_3_1 * term_3_3
    # In "softmax_loss_naive()"
    numer8r_minus = corrects_grad.dot(all_pre_grad)
    # NOTE: This numer8r_minus term was checked against "naive"s numer8r_minus term.  To great success.!
    #===================================================================================================

    #===================================================================================================
    # "numer8r_plus" :
    #     subterms 3_2 and 3_4 ("all_grad" and "corrects_pre_grad")
    #===================================================================================================
    numer8r_plus = all_grad_times__corrects_pre_grad = terms_3_2__and_3_4 =\
      (X.T).dot(                            # X.T.shape == (3073,500)
        (raw_softmax.T  *\
        raw_softmax[range(n_train),y]).T
      )
    # How to make sense of the intermediate terms:
    # raw_softmax[range(n_train),y] == "corrects_pre_grad"   (shape == (500,))
    # (raw_softmax.T).shape == (500,10)

    # If we can naively "divide out" (cancel) terms like we could in "vanilla" single-variate  "derivative over a quotient of f/g" algebra, this simple cancellation will work.  I'm like 70% sure this WON'T work, though.



    #===================================================================================================
    # Just an experiment:
    #===================================================================================================
    # plus:
    #===================================================================================================
    dW = \
      (X.T).dot(                            # X.T.shape == (3073,500)
        ((raw_softmax.T  /\
        denom.T) *\
        raw_softmax[range(n_train),y]).T
      ) # success rice!
    #===================================================================================================
    # minus:
    #===================================================================================================
    dW -=\
      corrects_grad.dot(
        all_pre_grad/\
        denom)
    #===================================================================================================
    # end "Just an experiment:"
    #===================================================================================================

    #===================================================================================================
    # average gradient:   so we divide by n_train:
    dW  /=  n_train
    #===================================================================================================
    # regularize
    dW += reg*W
    #===================================================================================================

    # Success!  (success rice)   Tested against "softmax_loss_naive"        (softmax_loss_naive(W, X, y, reg))              # right top buffer is "naive"

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    return loss, dW
###################################################################################################
# end func def "softmax_loss_vectorized(W, X, y, reg):"
###################################################################################################

#===================================================================================================
# old code below:
#===================================================================================================
# 1 idea for how to calcul8 dW (very simple, but all the details need to be worked out before we can actually implement this)
#dW =  (all_grad       / corrects_pre_grad) -\
#      (corrects_grad  / all_pre_grad)

# (x2 / x3) - (x1 / x4)

"""
#===================================================================================================
# "term_3_4" (AKA corrects_pre_grad) :
#===================================================================================================
all_sums = np.ones((n_train, n_classes))
x1=np.sum(raw_softmax, axis=ACROSS)                             # shape == (500,)         #   TODO: rename "x1" to something more descriptive
x2 = np.repeat(                                                 # shape == (3073, 500)    #   TODO: rename "x2" to something more descriptive
  x1.reshape(1,n_train),
  n_pix_vals, 
  axis=DOWN) 
corrects_pre_grad = term_3_4= x2.dot(all_sums)                                 # shape == (3073, 10)

#===================================================================================================
# "term_3_2" (AKA all_grad) :
#===================================================================================================
all_grad = term_3_2 = (X.T).dot(raw_softmax)
# (500,10) == raw_softmax.shape
# (  (3073, 500).dot ((500,10))  ) .shape == (3073, 10) == dW.shape
# 
# NOTE: This 3_2_term was checked against "naive"s 3_2_term.  To great success.!

#===================================================================================================
# "term_3_4" (AKA corrects_pre_grad) :
#===================================================================================================
#   TODO: rename lots of these variables
#===================================================================================================
x1 = raw[range(n_train), y]                                     # shape == (500,)         #   TODO: rename "x1" to something more descriptive
x2 = np.repeat(                                                 # shape == (3073, 500)    #   TODO: rename "x2" to something more descriptive
  x1.reshape(1, n_train),
  n_pix_vals,
  axis=DOWN)
corrects_pre_grad = term_3_4 = x2.dot(train_2_labels)                      # shape == (3073, 10)
"""

# I think it's *ACTUALLY* the 1st one:  ((x1 / x4) - (x2 / x3)),   not ((x2 / x3) - (x1 / x4))
# (x1 / x4) - (x2 / x3) 

"""
numer8r_plus = dW_term_3_2_j[:,j] * np.sum(dW_term_3_4[which_imgs_r_labeled_j]) # in this expression, 2nd_term.shape == (45,)

#numer8r_plus = np.random.random(numer8r_minus.shape)
# TODO FIXME FIXME
# TODO FIXME FIXME
numer8r = numer8r_plus - numer8r_minus # numer8r.shape == (45, 3073)
delta_W_j = np.sum((numer8r / denom), axis=DOWN)
#print("delta_W_j.shape: ", delta_W_j.shape)
dW[:,j] += delta_W_j
# denom.shape == (45,)
"""
'''





















































































