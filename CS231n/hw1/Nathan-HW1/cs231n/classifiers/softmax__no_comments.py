def softmax_loss_vectorized(W, X, y, reg):              # right mid buffer is "1 loop" version
    loss = 0.0
    dW = np.zeros_like(W) # same as np.zeros(W.shape) 

    num_train   = n_train   = X.shape[0]
    num_classes = n_classes = dW.shape[1]
    num_pix_vals= n_pix_vals= X.shape[1]

    SVM_scores=  scores= X.dot(W)         #(X.T).dot(W) # scores.shape==(N_train, 10)    ie. (500,10), for X_dev
    unnormalized_probs=np.exp(SVM_scores) # I also considered calling this variable "exps." 
    DOWN=0
    ACROSS=1
    probabilities= (unnormalized_probs.T /np.sum(unnormalized_probs, axis=ACROSS)).T  
    correct_probs=probabilities[range(num_train), y]

    tot_loss = np.sum(-np.log(correct_probs))
    loss = (tot_loss / num_train)
    loss += np.sum(0.5*reg*W*W)

    raw_softmax= exps= raw= unnormed= unnormalized_probs= unnormalized_probabilities= \
      np.exp(  X.dot(W)  )     # raw.shape == (500, 10)
    train_2_labels = np.zeros( scores.shape ) # (500,10)
    train_2_labels[range(n_train), y]=1

    scalars = np.exp(                   # scalars.shape == (500,)
      np.sum(
        W[:,y]* X.T,                    # X.T.shape == (3073, 500)
        axis=DOWN))
    corrects_grad = term_3_1= (X.T* scalars)
    all_pre_grad = term_3_3= np.sum(raw, axis=ACROSS) # (500,)
    denom = np.repeat(
      all_pre_grad.reshape((n_train,1)),
      n_classes,
      axis=ACROSS)
    denom = np.square(denom)
    all_pre_grad = (train_2_labels.T * all_pre_grad).T # all_pre_grad.shape == (500,10)

    numer8r_minus = corrects_grad.dot(all_pre_grad)
    numer8r_plus = all_grad_times__corrects_pre_grad = terms_3_2__and_3_4 =\
      (X.T).dot(                            # X.T.shape == (3073,500)
        (raw_softmax.T  *\
        raw_softmax[range(n_train),y]).T
      )

    # plus:
    dW = \
      (X.T).dot(                            # X.T.shape == (3073,500)
        ((raw_softmax.T  /\
        denom.T) *\
        raw_softmax[range(n_train),y]).T
      ) # success rice!

    # minus:
    dW -=\
      corrects_grad.dot(
        all_pre_grad/\
        denom)

    dW  /=  n_train
    dW += reg*W
    return loss, dW

def softmax_loss_naive(W, X, y, reg):                  # right top buffer is "naive"
    loss = 0.0
    dW = np.zeros_like(W) # same as np.zeros(W.shape) 
    num_train   = n_train   = X.shape[0]
    num_classes = n_classes = dW.shape[1]
    num_pix_vals= n_pix_vals= X.shape[1]
    SVM_scores=X.dot(W)         #(X.T).dot(W) # scores.shape==(N_train, 10)    ie. (500,10), for X_dev
    unnormalized_probs= raw= raw_softmax=np.exp(SVM_scores) # I also considered calling this variable "exps." 
    ACROSS=1
    probabilities= (unnormalized_probs.T /np.sum(unnormalized_probs, axis=ACROSS)).T  
    correct_probs=probabilities[range(num_train), y]

    # Calculate loss:
    tot_loss = np.sum(-np.log(correct_probs))
    loss = (tot_loss / num_train)
    loss += np.sum(0.5*reg*W*W)

    # Calculate grads (dW):
    import math
    for i in range(num_train):
        correct_class=y[i]
        dW_term_3_1 = X[i]* (math.e**(W[:, correct_class].dot(X[i]) ))
        dW_term_3_3 = np.sum (unnormalized_probs[i,:])
        dW_term_3_4 = unnormalized_probs[i, correct_class] # shape==1 (correct class' predicted score)
        quotient_rule_denom= dW_term_3_3 * dW_term_3_3 # squared

        for j in range(num_classes):
            dW_term_3_2  = X[i] * raw[i,j]
            numerator =   (dW_term_3_2 * dW_term_3_4) # old version with = - ...
            if j == correct_class:
                numerator-= (dW_term_3_1 * dW_term_3_3)
            dW[:,j] += (numerator / quotient_rule_denom)
    dW  /=  n_train
    dW += reg*W

    return loss, dW
