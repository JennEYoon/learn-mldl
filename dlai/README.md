# My exercises & practice - deeplearning.ai on Coursera.org  

#### Author: Jennifer E Yoon  

#### Class 1: Neural Networks  

Setup:  
  
  * Downloaded all materials for Class 1 and organized into correct folders.  
  * Read FORUM instructions for setup on local computer, but instructions mainly for Ubuntu on WSL.  
  * Seems rather simpler to just manually download files, and use Conda to install packages as needed.  
    Each notebook tells you which additional libraries need to be loaded.  
  * Ubuntu Conda3 python 3.7 produce error for plotting Matplotlib.  Investigate further. Check Coursera Matplotlib version. 
    - Coursera uses Python 3.6, programs installed in /opt/ folder. 

Notes:  

 * Week 1 in introduction to the concept of deep learning and history.  No homework.  
 * Week 2: Cat or no Cat notebook.  Binary classification, use logistic regression and sigmoid activation function.  
           - Also has tips on Numpy.  Mainly, do not use rank 1 array for column or row vector.  
             Always use rank 2.  [5, 1] or [1, 5] but not (5, ) or (5, ).T  
 * Week 3: Planar flower petals notebook.  Multiclass classification, use SKlearn, tanh activation function.  
 * Week 4: Culmination of all previous weeks of work. Fully connected neural network instructions.  
           - Building deep nn step by step notebook  
           - Deep neural network notebook  

#### Class 4: Convolutional Neural Networks  

  * Finished week 1, studying code notebook.  - 9/5/2019.  
  * Started week 2.  
  * Started week 3 videos - has interesting topics on transfer learning, data augmentation.  
  * To start week 4 Neural Style Transfer -- study for my website, articles.html post update.  
  * To start Papers -- Read paper on Neural Style Transfer for Art.  
  Q) Where is Greedy Adverserial Networks (GANs)?  
  Memo) Review "the deep learning book" math sections, CNN section.  

#### Class 5: Sequence Models (language recognition, speech processing)  
  * Understand how to build and train Recurrent Neural Networks (RNNs), and 
    commonly-used variants such as GRUs and LSTMs  
  

#### Tensorflow Class 1 and 2  

  * Uses Fashion MNist example, similar to Udacity Intro to TensorFlow class.  
  * [TensorFlow 2.0 Beta help](https://www.tensorflow.org/beta)  
  * Series also covers mobile app with TensorFlow-Lite.  
  * Seems very similar to what Udacity's class is trying to cover -- but is complete, whereas Udacity only has 6 weeks so far.  

#### Folder "source" has all downloaded notebook solutions and important papers.  

  * [source/Papers](https://github.com/JennEYoon/learn-mldl/tree/master/dlai/source/Papers)    
  * [Deep Face](https://github.com/JennEYoon/learn-mldl/blob/master/dlai/source/Papers/DeepFace.pdf)  
  * [Neural Style Transfer](https://github.com/JennEYoon/learn-mldl/blob/master/dlai/source/Papers/Neural_style_transfer.pdf)  

#### As part of the Deep Learning AI Specialization, there are videos on the early founders of deep learning.  

  * [Youtube Playlist](https://www.youtube.com/playlist?list=PLfsVAYSMwsksjfpy8P2t_I52mugGeA5gR)  
    
    ============================================      

## Other Resources  

#### 3 Blue 1 Brown on Neural Networks (4 videos).  

  * There is a very clear summary of neural networks by 3 Blue 1 Brown on YouTube.  
    It's a good summary of Class 1 and Class 4 of Coursera's DeepLearning.AI Specialization.  
    https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi  

#### Udacity - Intro to TensorFlow  

  * [Udacity - Intro to TF](https://www.udacity.com/course/intro-to-tensorflow-for-deep-learning--ud187)    
  * Class taught by Google team and Udacity coordinators.  
    Class is not complete.  In that sense Coursera's TensorFlow classes are better.  
  * [Comprehensive Guide to Convolutional Neural Nets ](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53). -- Finished reading.  
    Rather simple explanation.  Not as good as Coursera DeepLearning.AI or Fast.AI DeepLearning Part1.      
  * Finished first 4 weeks, weeks 5 and 6 left to go. - 9/5/2019.   
  * Uses Fashion MNIST notebook left to do -- similar to Coursera TensorFLow class.  
  * Weeks 5 & 6 to finish this month - 10/5/2019.  
  
#### fast.ai - Deep Learning classes  
[fast.ai main page](https://www.fast.ai/)  
 
Fast.ai is really good for those interested in practical applications and starting to do useful deep learning right away.  They want to democratize deep learning.  That is, allow a wider audience without a lot of coding or math backgrounds to start doing useful deep learning in many more application fields.  

 * deeplearning-part1: Practical Deep Learning for Coders 2019.  
    * The only pre-requisite is about 1 year of coding experience with Python.  
    * Uses custom package called "fastai" version 1.0 for 2019 classes.  
    * Fastai is built on top of PyTorch.  
    * Fastai package is also easy to read its source code.  
 
 * deeplearning-part2:  Deep Learning From the Foundations 2019.  
    * Teaches the foundations or under-the-hood coding from scratch.  
    * Lesson 8: Matrix multiplication; forward and backward passes
      https://course.fast.ai/videos/?lesson=8  
      This is good for deeply understandig how CNN works.  
    
 * 2018 version of deep learning classes.  
     http://course18.fast.ai/
 
   * Lesson 1 starts right off with transfer-learning.  
     http://course18.fast.ai/lessons/lesson1.html
      
     Transfer Learning is used to start off almost all modern convolutional neural network projects.  You download an already trained model with weights and filters.  You freeze the training layers.  You apply learning using your own date to only the last two fully-connected neural network layers with one softmax activation function in between.  Later, if you have sufficent data, you can unfreeze successive training layers and use your own data to train.  But at all times, you will start off with an already trained model to get the initial weights and initial convolution filters for each layer.  
 
   * Lesson 2 gets into data augmentation.  (2018 version, check if 2019 version also has this)  
     This is also a modern method applied to almost all situations.  
     http://course18.fast.ai/lessons/lesson2.html  
   
   * Started watching lesson 3.  To finish part 1 - 7 lessons this Fall 2019.   
 
--- end ---  

    
    
    
