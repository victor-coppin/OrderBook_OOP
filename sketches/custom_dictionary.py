"""
Create a custom dictionary like class
Allow :    
-extending the regular dictionary by adding new functionality
-modifying the standard dictionary's functionality/methods
Strategies :
1- inherit from an abstract class as MutableMapping
2- inherit from the Python built-in dict class directly
3- subclass UserDict fom collections
"""

# 2 Custom dictionary form dict class
"""
original built-in dict class 
can define new instance, static and class methods
store their instance attributes in a __slots__class attribute 
which replace the __dict__ attribute 
"""

class UpperCaseDict(dict):
    def __setitem__(self, key, value):
        key =key.upper()
        super().__setitem__(key, value)
numbers_dic = UpperCaseDict()
numbers_dic['One'] = 1
numbers_dic['two'] = 2
numbers_dic['ThREE'] = 3
print(numbers_dic)

# output : {'ONE': 1, 'TWO': 2, 'THREE': 3}

#without customization :
numbers_dictdefault = {}
numbers_dictdefault['One'] = 1
numbers_dictdefault['two'] = 2
numbers_dictdefault['ThREE'] = 3
print(numbers_dictdefault)

# output : {'One': 1, 'two': 2, 'ThREE': 3}

"""
The example above show an override of the __setitem__ method. 
"""
numbers_issues= UpperCaseDict({"onE":1, "Two":2, "tHree":3})
print(numbers_issues)
#output : {'onE': 1, 'Two': 2, 'tHree': 3}
#The class's initializer doesn't call __set__item() implicitly

"""
To avoid this initialization issue : 
"""

class UpperCaseDictCorrect(dict):
    def __init__(self, mapping=None,/,**kwargs):
        if mapping is not None:
            mapping = {
                str(key).upper():values for key, values in mapping.items()
            } #mapping is not None if for ex a dictionary is passed into UpperCaseDict_correct(dict)
        else :
            mapping = {}
        if kwargs:
            mapping.update(
                {str(key).upper(): values for key, values in kwargs.items()}
            ) #mapp the items provided, kwargs.items() is a tuple of the form ('a',1)
        super().__init__(mapping)

    def __setitem__(self, key, values):
        key = key.upper()
        super().__setitem__(key,values)

numbers_issues_correct= UpperCaseDictCorrect({"onE":1, "Two":2, "tHree":3})
print(numbers_issues_correct)

"""
Here, .__init__() converts the keys into uppercase letters and then initializes 
the current instance with the resulting data
It work for the setitem but not for other method like update method that need to 
be corrected too
Built-in Type were designed and implemented with open_closed principle in mind:
open to extension but closed to modification.
==> UserDict class could handle this problem
"""