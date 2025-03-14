#Script containing the classes used in the project

"""
Class Task
Models a single task in a software company's list of tasks.
Should have the following attributes:
 - description
 - an estimated number of hours for completion
 - the name of the programmer assigned to it
 - a status field to indicate if it is finished
 - a unique identifier
"""

class Task:

    __slots__ = ['description','workload','programmer','__done_status','id'] #avoid dynamic creation of attributes

    def __init__(self,task_description,estimated_hours_for_completion,programmer_assigned_name):
        self.description = task_description
        self.workload = estimated_hours_for_completion
        self.programmer = programmer_assigned_name


        self.__done_status = "NOT_FINISHED"

x = Task("ajout metaclass",29,"victor")
print(x.description)
x.prenom = "coppin"
print(x.prenom)