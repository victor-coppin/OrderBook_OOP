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
        """
        #Description
        if 0< len(description.split()) < 12:
            self.__description = description
        else:
            raise ValueError("erroneous input")
        # Workload
        if isinstance(workload, int):
            self.__workload = workload
        elif isinstance(workload, str): #try to convert text to int, ex 4,4 => 4
            try :
                workload = workload.replace(',', '.')
                self.__workload= round(float(workload))
            except Exception:
                raise Exception("erroneous input")
        else:
            raise ValueError("erroneous input")
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
    @property
    def id_number(self):
        return self.__id_number
    """
    Class Methods
    """
    @classmethod # class method that allow to use the following method without reference to an instance.
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

    def __str__(self):
        if self.workload == 1:
            return (str(self.__id_number) + ": " + self.description + " (" + str(self.workload) + " hour),"
                    + " programmer " + self.programmer + " " + self.__done_status)
        else:
            return (str(self.__id_number) + ": " + self.description + " (" + str(self.workload) + " hours),"
                + " programmer " + self.programmer +" "+self.__done_status)



"""
Class OrderBook
The orderbook that used to store, add and query tasks 
"""
class OrderBook(Task):
    def __init__(self):
        super().__init__(description="add description", programmer="add your name",workload=0)
        self.order_dictionary = {} #contains all the order's instances with the order.id as a key
        self.order_dictionary_programmer = {} #contain the numbers of finished, not-finished, and respective hours to complete
        self.orderID_finished = [] #list all finished. Filled within the mark_finished method
        self.orderID_not_finished = []

    def add_order(self, description, programmer, workload):
        order = Task(description, programmer, workload)
        self.order_dictionary[order.id_number] = order #add the new order in the dictionary with the key as the id
        self.orderID_not_finished.append(order.id_number) #add ID of the task to the orderID_not_finished list
        if programmer not in self.order_dictionary_programmer.keys():
            self.order_dictionary_programmer[programmer] = [[order.id_number],0,1,0,order.workload]
        else:
            self.order_dictionary_programmer[programmer][0].append(order.id_number)
            self.order_dictionary_programmer[programmer][2] += 1
            self.order_dictionary_programmer[programmer][4] += order.workload
        return order

    def __str__(self,programmer_orders = False):
        return super().__str__()

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
        self.order_dictionary_programmer[programmer][3] += int(workload)
        self.order_dictionary_programmer[programmer][4] -= int(workload)
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



print(int(round(float(0.4))))

# orders = OrderBook()
# orders.add_order("this is i hope a very very long be ", "Adele", 10)
# orders.add_order("program mobile app for workload accounting", "Eric", 25)
# orders.add_order("program app for practising mathematics", "Adele", 100)
# print(orders.order_dictionary_programmer.keys())
# print(orders.orderID_not_finished)
# not_finished_tasks = [orders.order_dictionary[id_num] for id_num in orders.orderID_not_finished]
# for order in not_finished_tasks:
#     print(order)
# finished_tasks = [orders.order_dictionary[id_num] for id_num in orders.orderID_finished]
# for order in finished_tasks:
#     print(order)
# for order in orders.all_orders ():
#     print(order)
# print(orders.programmers_list_tasks())
# print(orders.order_dictionary_programmer)
# orders.mark_finished(1)
# orders.mark_finished(2)
# print(orders.order_dictionary_programmer)
# for order in orders.all_orders ():
#     print(order)
# print(orders.status_of_programmer("Adele"))
# print(orders.status_of_programmer("Eric"))
# for programmer in orders.programmer():
#     print(programmer)
# print(orders.programmers_list_tasks())