# My notes from Optimization  

#### alpha - learning rate
  * If alpha is too big from the start - can overshoot optimal minimum point.  
  * If alpha is too small from the start - takes too long to converge to solution.  

#### number of minibatches, L - number of layers  
  * twick number of minibatches, number of layers

#### Batch Normalization  

Z-values, every level per layer normalize. No one feature blows away other features.  
Change scale so no one feature dominates result with high values. 


Ng - Always uses "Adam optimizer", much better than others, 94% accuratcy usually.  
Ng - Default values for Beta1, Beta2, epsilon.  Almost neve change these.  
Beta1 = 0.9 (use only last 10 recent history, rapidly converges to new data point)  
Beta2 = 0.999  (second order calculation, average of sqaures of gradients), polynomial expansion.  
epsilon = small number to take care of divide by zero edge case.  Convert integer to float. 
