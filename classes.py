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
    id_counter = 0 # class attribute that will be used to create a unique ID
    __slots__ = ['description','workload','programmer','__done_status','id'] #avoid dynamic creation of attributes

    def __init__(self,task_description,estimated_hours_for_completion,programmer_assigned_name):
        self.description = task_description
        self.workload = estimated_hours_for_completion
        self.programmer = programmer_assigned_name

        type(self).id_counter += 1 # incrementation of the id_counter
        self.__done_status = "NOT_FINISHED"
        self.id = type(self).id_counter

"""
Change the behavior of the id by made it private with a get method 
be carefully to avoid decrease of the id_counter : if one task is complete, counter //
shouldn't decrease --> if a task is complete the function to count the number of tasks //
should count the number of tasks with the status NOT_FINISHED
"""




