#Script containing the classes used in the project

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
        self.__id = type(self).__id_generator #type(self) is used in case class name is changed:i.e. avoid Task.id
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
    def id(self):
        return self.__id
    @id.setter #used for the unit test
    def id(self,x):
        self.__id = x



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
        return (str(self.id) + ": " + self.description + " (" + str(self.workload) + " hours),"
                + " programmer " + self.programmer +" "+self.__done_status)


class OrderBook:
    def __init__(self):
        self.__tasks = []
    def add_order(self, description, programmer, workload):
        task = Task(description, programmer, workload)
        self.__tasks.append(task)





















t1 = Task("program hello world","Eric",3)
print(t1.id,t1.description, t1.programmer, t1.workload)
print(t1)
print(t1.is_finished())
t1.mark_finished()
print(t1)
print(t1.is_finished())
t2 = Task("program webstore", "Adele", 10)
t3 = Task("program mobile app for workload accounting", "Eric", 25)
print(t2)
print(t3)



