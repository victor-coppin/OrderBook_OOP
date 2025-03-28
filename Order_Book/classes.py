"""
Class Task
Models a single task in a software company's list of the tasks.
"""

class Task:
    __id_generator = 0 # class attribute that will be used to create a unique ID
    """__slots__ = ['description','workload','programmer','__done_status','id'] #avoid dynamic creation of attributes"""

    def __init__(self, description, programmer, workload):
        """
        Task to complete
        should provide a short description, your name and the estimated hours for completion(int).
        """

        if len(description.split()) < 20:
             self.__description = description
        else:
            raise ValueError("Description is too long ! Remember Agile best practice and keep it short.")

        if type(workload) == int:
            self.__workload = workload
        else:
            raise ValueError("workload should be an integer")

        self.__programmer = programmer

        type(self).__id_generator += 1 # incrementation of the id_generator
        self.__id_number = type(self).__id_generator #type(self) is used in case class name is changed:i.e. avoid Task.id
        self.__done_status = "NOT FINISHED" # think if better to stock as a boolean

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
    """
    Instance Methods 
    """
    def is_finished(self):  # getter that return a boolean by compare the __done_status's value
        return self.__done_status == "FINISHED"

    def mark_finished(self):
        self.__done_status = "FINISHED"

    def __str__(self):
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
        self.order_dictionary_programmer = {} #contains a tuple that represent tasks for programmers as key
    def add_order(self, description, programmer, workload):
        order = Task(description, programmer, workload)
        self.order_dictionary[order.id_number] = order
        self.order_dictionary_programmer[programmer] = []
        self.order_dictionary_programmer[order.programmer].append((order.id_number,order.description, order.workload))
        return order

    def __str__(self,programmer_orders = False):
        return super().__str__()
    def all_orders(self):
        return self.order_dictionary.values()

    def programmer(self):
        return self.order_dictionary_programmer.keys()
    # def programmer_task(self):
    #         str()self.order_dictionary_programmer.keys()

orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)
for programmer in orders.programmer():
    print(programmer)


