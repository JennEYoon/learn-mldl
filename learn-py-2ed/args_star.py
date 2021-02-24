# Variable number, positional argument 
#  - function definition  

# args_star.py -- this file  
# trailing underscor, e.g., min_ , is used to limit confusion with 
# commonly used names in Python, e.g., min( ), Python built-in function. 

def minimum(*n):  
    print(type(n))  # tuple  
    if n:  
        # If n exists, if True.   
        min_ = n[0] 
        for x in n[1:]:
            if x < min_: 
                min_ = x 
        print("calc=", min_)
    else:  
        print('n/a') 	

# Run function.  
minimum(1, 3, 5, -2, -4)  # Should return -4.  
minimum(3.5, 2.5)  # Should return 2.5.  
minimum()  # Should return 'n/a'. 

""" output  
<class 'tuple'>                                                                                                         calc= -4                                                                                                                <class 'tuple'>                                                                                                         calc= 2.5                                                                                                               <class 'tuple'>                                                                                                         n/a     

"""