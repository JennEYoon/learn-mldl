## Tasks for Tensor Flow class -- deeplearning.ai, Coursera.org  

>Note: Exercise notebooks are locked for auditors, but I downloaded them from a student's Github page.

#### Week1:

 * Hello World notebook  
    * Notebook Github link  	
    https://github.com/lmoroney/dlaicourse/blob/master/Course%201%20-%20Part%202%20-%20Lesson%202%20-%20Notebook.ipynb
    * CoLab link      
    https://colab.sandbox.google.com/github/lmoroney/dlaicourse/blob/master/Course%201%20-%20Part%202%20-%20Lesson%202%20-%20Notebook.ipynb
 
 * Tensor Flow Playpen notebook (demo)  
 
 * Housing Price prediction notebook  
   https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Exercises/Exercise%201%20-%20House%20Prices/Exercise_1_House_Prices_Question.ipynb  
   
  * Exercise  
    https://github.com/JennEYoon/learn-mldl/blob/master/dlai/tensorflow/Exercises/Exercise%201%20-%20House%20Prices/Exercise_1_House_Prices_Answer.ipynb
 
 #### Week2:
 
  * Fashion MNIST dataset  
     https://www.kaggle.com/zalando-research/fashionmnist  
     ```python
     mnist = tf.keras.datasets.fashion_mnist
     ```

>Content
Each image is 28 pixels in height and 28 pixels in width, for a total of 784 pixels in total. Each pixel has a single pixel-value associated with it, indicating the lightness or darkness of that pixel, with higher numbers meaning darker. This pixel-value is an integer between 0 and 255. The training and test data sets have 785 columns. The first column consists of the class labels (see above), and represents the article of clothing. The rest of the columns contain the pixel-values of the associated image.

>To locate a pixel on the image, suppose that we have decomposed x as x = i * 28 + j, where i and j are integers between 0 and 27. The pixel is located on row i and column j of a 28 x 28 matrix.
For example, pixel31 indicates the pixel that is in the fourth column from the left, and the second row from the top, as in the ascii-diagram below. 

  * Machine Learning Fairness  
    https://developers.google.com/machine-learning/fairness-overview/
