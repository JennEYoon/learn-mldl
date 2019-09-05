# Meetup Links to Working Code, Stanford cs231n 

# Assignment 2 and 3:  

### Nathan Bendich has finished Assignments 2 and 3

  https://github.com/neonb88/cs231n_spring_2019    
 
  See his website for solutions to all 3 assignments.  
  Thank you, Nathan!   
  Updated as of 8/29/2019.
  
   **Nathan Bendich 8:26 PM Sept 4, 2019**  
   "It's very funny to be reading this 1-2 months after I did HW2 when I've probably forgotten  
    at least 1/3 of the details.  I'm glad it's been helpful.  There are many other github  
    repositories that are better-commented than mine and other tutorials I found super helpful.  
   **Andrej Karpathy** explained everything well quite thorough in his explanations of the fundamentals.  
    * [nn-case-study](http://cs231n.github.io/neural-networks-case-study/)  
    * [optimization-2](http://cs231n.github.io/optimization-2)"  
      ... Quoted from a Slack.com message. ...  

# Assignment 1:   

### Chris Malec:  (Chris posted that he finished all parts as of 7/29/2019)

   https://github.com/cemalec/CS231/blob/master/assignment1/  
   
   knn, svm, softmax, 2 layer nn:  
   https://github.com/cemalec/CS231/blob/master/assignment1/knn.ipynb  
   https://github.com/cemalec/CS231/blob/master/assignment1/svm.ipynb  
   https://github.com/cemalec/CS231/blob/master/assignment1/softmax.ipynb  
   https://github.com/cemalec/CS231/blob/master/assignment1/cs231n/classifiers/neural_net.py  
   https://github.com/cemalec/CS231/blob/master/assignment1/two_layer_net.ipynb  
   
   Math for svm, softmax, Back Prop:  
   https://cemalec.github.io/main/    
   
   https://cemalec.github.io/Gradients_Softmax/  
   https://cemalec.github.io/Gradients_Hingeloss/  
   ttps://cemalec.github.io/Gradients_NN/ (edited)   
   
   
### Colleen Chen:  

   https://github.com/colleen-chen/learn--cs231n-
    
 - Two layer nn:  (Updated link from Colleen, as of 7/31/2019.)  
   https://github.com/colleen-chen/learn--cs231n-/tree/master/classifier/neural_net.py  
   
   https://github.com/colleen-chen/learn--cs231n-/blob/master/classifier/neural_net.py
   
### Nathan Bendich:     

   2 layer nn in zip file:  
   https://www.dropbox.com/s/llgiwyqril6ljms/cs231n_assn1___working_2-deep_NN.tar.xz?dl=0 . 
   
   You can probably just "double-click" on the file name too and something will pop up to decompress it.  
   Please let me know if you have any questions.  I can try to explain as best as possible while I'm not working 
   on the next part of the assignment.   
   >tar -xvf cs231n_assn1___working_2-deep_NN.tar.xz  (to unzip)  
   

### Peter 

   softmax code part of codeshare file: 
   [codeshare_hw1b.py](codeshare_hw1b.py)


### Jennifer Yoon -- to add  

    To add my knn blog post & algo.py links
    To add Vanderplas fancy indexing and argsort numpy link

### Any others?  

   

### Resources  

**Jennifer:** Bishop, Pattern Rec & ML,  c2006.  
Chp 5 is math of Neural Networks (p 225 book, p 245 in PDF format).  
http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf

**Colleen:** Coursera, deeplearning.ai, class 1, back-prop:  
https://www.coursera.org/learn/neural-networks-deep-learning/lecture/6dDj7/backpropagation-intuition-optional  

**Jennifer:** Coursera, deeplearning.ai, class4, activation-functions:  
https://www.coursera.org/learn/neural-networks-deep-learning/lecture/4dDC1/activation-functions  

**Nathan:** "The partial derivatives for the softmax are hard to derive by hand.  For the 2-layer fully-connected NN, it took me many many pages of notes.  Please keep going even if you have to write out pages and pages of notes over multiple days to understand it.  I had to.   One of the annoying points is that almost nothing is a scalar; everything is a vector, matrix, or higher rank tensor.  So to properly do the partial derivatives you have to take something this guy Eli Bendersky calls the Jacobian: https://eli.thegreenplace.net/2016/the-softmax-function-and-its-derivative/ "  

**Andrew D:** Do CIFAR-10 Classifiers Generalize to CIFAR-10?  https://arxiv.org/abs/1806.00451  

**Andrew D:**  Tensorflow library automatically loads famous datasets into numpy arrarys.
https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10/load_data
