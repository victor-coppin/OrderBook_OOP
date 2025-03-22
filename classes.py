#Script containing the classes used in the project

"""
Class Task
Models a single task in a software company's list of the tasks.
"""

class Task:
    __id_counter = 0 # class attribute that will be used to create a unique ID
    __slots__ = ['description','workload','programmer','__done_status','id'] #avoid dynamic creation of attributes

    def __init__(self, description, programmer, workload):
        """
        Task to complete
        should provide a short description, your name and the estimated hours for completion(int).
        """
        self.add_order(description,programmer, workload)

    def add_order(self,description,programmer, workload):
        if len(description.split()) < 20:
            self.description = description
        else:
            raise ValueError("Description is too long ! Remember Agile best practice and keep it short.")

        if type(workload) == int:
            self.workload = workload
        else:
            raise ValueError("workload should be an integer")

        self.programmer = programmer
        type(self).__id_counter += 1 # incrementation of the id_counter
        self.id = type(self).__id_counter #type(self) is used in case class name is changed:i.e. avoid task.id
        self.__done_status = "Not_Finished"

    @property
    def is_finished(self): #getter that return a boolean by compare the __done_status's value
        return  self.__done_status == "Finished"

    """
    Methods
    """
    @classmethod # class method that allow to use the following method without reference to an instance.
    def number_of_tasks(cls):
        return cls.__id_counter

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

