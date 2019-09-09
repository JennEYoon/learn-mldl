## Meetup Links to Working Code, Stanford cs231n 


### Nathan Bendich has finished Assignments 1, 2 and 3

  * https://github.com/neonb88/cs231n_spring_2019    
 
  See his website for solutions to all 3 assignments.  
  Thank you, Nathan!  Updated as of 8/29/2019.
  
   >**Nathan Bendich 8:26 PM Sept 4, 2019**  
   "It's very funny to be reading this 1-2 months after I did HW2 when I've probably forgotten at least 1/3 of the details.  I'm glad it's been helpful.  There are many other github repositories that are better-commented than mine and other tutorials I found super helpful.  

   >**Andrej Karpathy** explained everything well quite thorough in his explanations of the fundamentals.  
    * [nn-case-study](http://cs231n.github.io/neural-networks-case-study/)  
    * [optimization-2](http://cs231n.github.io/optimization-2)"  
      ... Quoted from a Slack.com message. ...  

   >**Nathan Resources:** "The partial derivatives for the softmax are hard to derive by hand.  For the 2-layer fully-connected NN, it took me many many pages of notes.  Please keep going even if you have to write out pages and pages of notes over multiple days to understand it.  I had to.   One of the annoying points is that almost nothing is a scalar; everything is a vector, matrix, or higher rank tensor.  So to properly do the partial derivatives you have to take something this guy Eli Bendersky calls the Jacobian: https://eli.thegreenplace.net/2016/the-softmax-function-and-its-derivative/ "  


### Chris Malec:  (Finished all HW #1 in July and most of HW #2 in August.)

 * https://github.com/cemalec/CS231/blob/master/assignment1/   
 * https://cemalec.github.io/main/   
   
   **knn, svm, softmax, 2 layer nn:**  
   https://github.com/cemalec/CS231/blob/master/assignment1/knn.ipynb  
   https://github.com/cemalec/CS231/blob/master/assignment1/svm.ipynb  
   https://github.com/cemalec/CS231/blob/master/assignment1/softmax.ipynb  
   https://github.com/cemalec/CS231/blob/master/assignment1/cs231n/classifiers/neural_net.py  
   https://github.com/cemalec/CS231/blob/master/assignment1/two_layer_net.ipynb  
   
   **Math for svm, softmax, Back Prop:**  
   https://cemalec.github.io/Gradients_Softmax/  
   https://cemalec.github.io/Gradients_Hingeloss/  
   https://cemalec.github.io/Gradients_NN/     
   
   
### Colleen Chen:  

 * https://github.com/colleen-chen/learn--cs231n-
    
 * Two layer nn:  (Updated link from Colleen, as of 7/31/2019.)  
   https://github.com/colleen-chen/learn--cs231n-/tree/master/classifier/neural_net.py  
   https://github.com/colleen-chen/learn--cs231n-/blob/master/classifier/neural_net.py
   
 * Coursera, deeplearning.ai, class 1, back-prop:  
https://www.coursera.org/learn/neural-networks-deep-learning/lecture/6dDj7/backpropagation-intuition-optional  


### Peter:  

 * softmax code part of codeshare file: 
   [codeshare_hw1b.py](codeshare_hw1b.py)


### Jennifer Yoon Resources:     

 * Excellent blog on K-nearest neighbor with CIFAR10 dataset.  
    Akash Goswami, Feb 8, 2018, "Introduction to image classification with knn"  -- https://medium.com/@YearsOfNoLight/intro-to-image-classification-with-knn-987bc112f0c2
   
   Full notebook for knn  --
https://github.com/adotg/knn-what-how-why/blob/develop/knn.ipynb
   
   Python code only, knn_algo.py  --
https://github.com/adotg/knn-what-how-why/blob/master/knn_algo.py

 * KNN argsort and indexing resource - VanderPlas book, Numpy chapter.  
   Page 65 starts off Numpy Broadcasting, and knn argsort() is on page 88. 
   https://books.google.com/books/about/Python_Data_Science_Handbook.html?id=6omNDQAAQBAJ&printsec=frontcover&source=kp_read_button#v=onepage&q&f=false

 * Great Math SVM source, this one from MIT.
https://www.youtube.com/watch?v=_PwhiWxHK8o
Remember that W vector is perpendicular to the hyperplane we are looking for.  We actually solve for this W vector to get the hyperplane.

 * Math for svm:  https://shuzhanfan.github.io/2018/05/understanding-mathematics-behind-support-vector-machines/
 * Algorithm for svm:  
   https://www.csie.ntu.edu.tw/~cjlin/papers/quadworkset.pdf  

   libsvm is the support vector machine implementation in scikit-learn, and has lots of help documents from total newbie to advanced reader.  https://www.csie.ntu.edu.tw/~cjlin/libsvm/  

 * Bishop, Pattern Rec & ML,  c2006.  
Chp 5 is math of Neural Networks (p 225 book, p 245 in PDF format).  
http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf

 * Coursera, deeplearning.ai, class4, activation-functions:  
https://www.coursera.org/learn/neural-networks-deep-learning/lecture/4dDC1/activation-functions  
   

### Andrew Draganov Resources:  

 * Do CIFAR-10 Classifiers Generalize to CIFAR-10?  https://arxiv.org/abs/1806.00451  

 * Tensorflow library automatically loads famous datasets into numpy arrarys.
https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10/load_data

 * Intro class - Neural Networks in Application.  
   https://github.com/Andrew-Draganov/Neural-Networks-in-Application/  