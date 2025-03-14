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
    def __init__(self,task_description,estimated_hours_for_completion,programmer_assigned_name,execution_status):
        self.description = task_description
        self.estimated_hours = estimated_hours_for_completion
        self.programmer_name = programmer_assigned_name
        self.done_status = execution_status
        # need to think about uniq id
    pass

x = Task("hello", 10, "victor", "NOT FINISHED")
print(x)

