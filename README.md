Order book
Application that collects all tasks for a software company.

<img alt="Diagram_OrderBook.drawio.png" height="300" src="Diagram_OrderBook.drawio.png" width="500"/>

**Containers:** 
While class order inherit from the Task() class, the main mechanism 
is the research method to get the task for a programmer or by status:
although create 2 dictionaries and 2 lists, increase the memory management,
it was design to iterate quickly  to iterate just the relevant IDs rather
than check for each task.
Each time a task is adding to the OrderBook, it is saved in an order dictionary
with the id's as the key, and in another one with the programmer for the key.
it also save the id inside a not finish list that wil be used to iterate only
on the remaining task.
marked finish on a task will delete it from the not finished list and place it on
a second list,  


**Handle errors:** 
Try to manage instantiations errors by handling errors in the task class:
-prevent modifications by adding only getters
-description are filter to be short to keep it "Agile"
-workload are parse to be integer or float

Other handling errors are on the main program to check the user input only.

In addition to learn OOP, this project help me to look at the different techniques to stock data, 
add test and practicing Git.






