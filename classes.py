#Script containing the classes used in the project

"""
Class Task
Models a single task in a software company's list of the tasks.
"""

class Task:
    __id_generator = 0 # class attribute that will be used to create a unique ID
    __slots__ = ['description','workload','programmer','__done_status','id'] #avoid dynamic creation of attributes

    def __init__(self, description, programmer, workload):
        """
        Task to complete
        should provide a short description, your name and the estimated hours for completion(int).
        """

        if len(description.split()) < 20:
            self.description = description
        else:
            raise ValueError("Description is too long ! Remember Agile best practice and keep it short.")

        if type(workload) == int:
            self.__workload = workload
        else:
            raise ValueError("workload should be an integer")

        self.__programmer = programmer

        type(self).__id_generator += 1 # incrementation of the id_generator
        self.__id = type(self).__id_generator #type(self) is used in case class name is changed:i.e. avoid Task.id
        self.__done_status = "Not_Finished" # think if better to stock as a boolean

    @property #encapsulation
    def description(self):
        return self.__description
    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def programmer(self):
        return self.__programmer

    @property
    def workload(self):
        return self.__workload
    @property
    def id(self):
        return self.__id


    @property
    def is_finished(self): #getter that return a boolean by compare the __done_status's value
        return  self.__done_status == "Finished"

    """
    Methods
    """
    @classmethod # class method that allow to use the following method without reference to an instance.
    def number_of_tasks(cls):
        return cls.__id_generator

    def mark_finished(self):
        self.__done_status = "Finished"

    def __str__(self):
        return str(self.id) + ": " + self.description + " (" + str(self.workload) + "hours)," + " programmer " + self.programmer

x = Task("long to read for a card","Eric",4)
print(x)
print(Task.number_of_tasks())
print(x.number_of_tasks())
print(x.is_finished)
x.mark_finished()
print(x.is_finished)
print(x.id)
w = Task("long to read for a card","Eric",3)
print(w)

