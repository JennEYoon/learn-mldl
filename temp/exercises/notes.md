# Notes reading Fluent Python.  
Notebook exercises here too.  

### Chp 1 Dunder Method, Special Method:  

Takes a long time to understand Special Methods.  
In Python, they are implemented in low-level, oftern in CPython Interpreter.  

>```__getter__(self):  ```  
>Allows ```obj.__getter__(self)``` to be called, and returnes ```self.method(obj)```.  

Square bracket, [ ], works in Python with Collections and NamedTuples to turn 
user defined object into indexed & iterable list.  All built-in definitions of LIST 
can then be used with the User Defined object.  

>card[0] >>> returns card rank,  
>card[1] >>> returns card suit.  

deck[0] >>> returns Card(rank='2', suit='diamonds'), 
Used defined instance of a Card class object with its attributes, in order.  

deck[-1] >>> returns Card(rank='A', suit='spades')  

deck[13::13] >>> returns all Ace cards.  

LIST has built-in definitions for:  
  * indexing  
  * reversed indexing  
  * sorted  
  * slice notation (with start, stop, steps) 

Code random.choice(deck) >>> returns a randomly chosen card.  
Python RANDOM pkg works with LIST to add more functionality.  

### namedtuple can't take assignment  
   * collections.namedtuple does not allow ```__setter__()```  method after initialization.  
   * can create another instance of namedtuple with new elements.  
   * tuples can't be changed
   
 ```Card = collections.namedtuple('Card', ['rank', 'suit'])```  
 Namedtuple presumably takes **Name and Tuple** elements.  
 Card class can be redefined using list and dict, instead of namedtuple module.   
 Try it.  Compare.  
   
#### 6/17/2020 1:40 AM, working on Card class def  
  * Forgot how to create class.  
  * Cread card and deck class from scratch -- w/o help, only Class obj information.  
  
#### 6/21/2020, class object  
  * "class" is keyword for creating class, not "def" which is for functions.  
  * ```class MyClass: ``` (without () for class that has no inheritance).  
  * ```def __init__(self): ``` for instance function definition.  
  

