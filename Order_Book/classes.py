import math
import pickle
"""
Class Task
Models a single task in a software company's list of the tasks.
"""
class Task():
    __id_generator = 0 # class attribute that will be used to create a unique ID
    def __init__(self, description, programmer, workload):
        """
        Task to complete
        should provide a short description, your name and the estimated hours for completion(int).
        description : a short description of the task, less than 12 worlds
        programmer: first-name of the programmer, must be without space
        workload: workload of the task, int or float
        Handle exceptions :
        While instantiate, check the type of each argument
        """
        #Description
        if 0< len(description.split()) < 12: #avoid long descriptions
            self.__description = description
        else:
            raise ValueError("erroneous input: need a short ( <12 words) description")
        # Workload
        if isinstance(workload, int):
            self.__workload = workload
        elif isinstance(workload, str): #if strings, try to convert text to float, ex 4,4 => 4.4
            try:
                workload = workload.replace(',', '.')
                workload = float(workload)
            except (TypeError, ValueError):
                raise ValueError("erroneous input: workload must be int or float")
            else: self.__workload = workload
        else:
            raise ValueError("erroneous input: workload must be a number")
        #Programmer
        if programmer is None:
            raise ValueError("erroneous input")
        else:
            self.__programmer = programmer

        type(self).__id_generator += 1 # incrementation of the id_generator
        self.__id_number = type(self).__id_generator #type(self) is used in case class name is changed:i.e. avoid Task.id

        self.__done_status = "NOT FINISHED" #hardcode the value of the status when initialize

    """
    Getter of the private attributes / no setters to avoid mistake
    """
    @property #encapsulation
    def description(self):
        return self.__description
    @property
    def programmer(self):
        return self.__programmer
    @property
    def workload(self):
        return self.__workload
    @workload.setter
    def workload(self, value):
        self.__workload = value
    @property
    def id(self):
        return self.__id_number
    """
    Class Methods
    """
    @classmethod
    def number_of_tasks(cls):
        return cls.__id_generator
    @classmethod
    def id_generator_to_zero(cls):
        cls.__id_generator = 0
    """
    Instance Methods 
    """
    def is_finished(self):  # getter that return a boolean by compare the __done_status's value
        return self.__done_status == "FINISHED"

    def mark_finished(self):
        self.__done_status = "FINISHED"

    def __repr__(self):
        return f'Task({self.description}, {self.programmer}, {self.workload})'

    def __str__(self):
        if self.workload == 1:
            return (str(self.__id_number) + ": " + self.description + " (" + str(self.workload) + " hour),"
                    + " programmer " + self.__programmer + " " + self.__done_status)
        else:
            return (str(self.__id_number) + ": " + self.description + " (" + str(self.workload) + " hours),"
                    + " programmer " + self.__programmer + " " + self.__done_status)



"""
Class OrderBook
The orderbook that used to store, add and query tasks 
"""
class OrderBook(Task):
    def __init__(self,description="add description", programmer="add your first-name",workload="0"):
        super().__init__(description, programmer,workload)
        self.order_dictionary = {} #contains all the order's instances with the order.id as a key
        self.order_dictionary_programmer = {} #contain the numbers of finished, not-finished, and respective hours to complete
        self.orderID_finished = [] #list all finished. Filled within the mark_finished method
        self.orderID_not_finished = []
        self.__id_generator = 0 #this implies that each orderbook have its own counter
    def add_order(self, description, programmer, workload):
        if isinstance(workload,str):
            try:
                workload = workload.replace(',', '.')
                workload = float(workload)
                workload = math.ceil(workload) #round to the up : 3,4 => 4
            except (TypeError, ValueError):
                raise ValueError("erroneous input: workload must be int or float")
        elif isinstance(workload,int or float):
            workload = math.ceil(workload)
        else:
            raise ValueError("erroneous input: workload must be a int or float")
        order = Task(description, programmer, workload)
        self.order_dictionary[order.id] = order #add the new order in the dictionary with the key as the id
        self.orderID_not_finished.append(order.id) #add ID of the task to the orderID_not_finished list
        if programmer not in self.order_dictionary_programmer.keys():
            self.order_dictionary_programmer[programmer] = [[order.id],0,1,0,workload]
        else:
            self.order_dictionary_programmer[programmer][0].append(order.id)
            self.order_dictionary_programmer[programmer][2] += 1
            self.order_dictionary_programmer[programmer][4] += workload
        return order


    def all_orders(self):
        return self.order_dictionary.values()
    def programmer(self):
        return self.order_dictionary_programmer.keys()
    def programmers_list_tasks(self):
        programmers_list = {}
        for programmer,info in self.order_dictionary_programmer.items():
            programmers_list[programmer] = info[0]
        return  programmers_list
    def mark_finished(self,order_id=0):
        """
        A method that takes the id of the task as its argument and marks the relevant task as
        finished. If there is no task for the given id, the method should raise a ValueError
        exception.
        """
        self.order_dictionary[order_id].mark_finished()
        programmer = self.order_dictionary[order_id].programmer
        workload = self.order_dictionary[order_id].workload
        self.order_dictionary_programmer[programmer][1] += 1
        self.order_dictionary_programmer[programmer][2] -= 1
        self.order_dictionary_programmer[programmer][3] += workload
        self.order_dictionary_programmer[programmer][4] -= workload
        self.orderID_finished.append(order_id) # fill a list with the id of finished task
        self.orderID_not_finished.remove(order_id)

    def list_task_not_finished(self):
        if len(self.orderID_not_finished) == 0:
            print("no unfinished tasks")
        else:
            for order_id in self.orderID_not_finished:
                print(self.order_dictionary[order_id])

    def list_task_finished(self):
        if len(self.orderID_finished) == 0:
            print("no finished tasks")
        else:
            for order_id in self.orderID_finished:
                print(self.order_dictionary[order_id])

    def status_of_programmer(self,programmer):
        return tuple(self.order_dictionary_programmer[programmer][1:5])

    #save the current instantiation of the orderbook as an object
    def save_orderbook(self,orderbook_backup = "orderbook.pkl"):
        with open(orderbook_backup,"wb") as save:
            pickle.dump(self, save)
            save.close()

    @classmethod
    def load_orderbook(cls,orderbook_backup = "orders.pkl"):
        with open(orderbook_backup,"rb") as load:
            return pickle.load(load)
