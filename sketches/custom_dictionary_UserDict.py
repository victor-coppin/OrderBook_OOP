from collections import UserDict
"""
UserDict was created back when it was impossible to inherit from Python's
dictionary directly without error. 
It is a convenient wrapper around a regular dict object. 
This class provide same behavior as built-in dict with the additional feature of giving
you access to the underlying data structure through the .data instance attribute.
UserDict was specially designed for subclassing purposes : it allows you to create
dictionary-like classes through inheritance.
"""

class UpperCaseDict(UserDict):
    def __setitem__(self,key,value):
        key = key.upper()
        super().__setitem__(key,value)

upper_case_dict = UpperCaseDict({"one":1, "tWo":2, "tHree":3})
print(upper_case_dict)

"""
With the UserDict, the class works correctly and didn't need to provide a custom
implementation of the __init__ method 
"""

"""
Practical example of a dictionary like class :
A dictionary that Accepts British and American Spelling of Keys 
"""
UK_TO_US = {"colour": "color", "flavour": "flavor", "behaviour": "behavior"}
# constant that contain the british as key and the matching american words as values
class EnglishSpelledDict(UserDict):
    def __getitem__(self,key):
        try :
            return self.data[key]
        except KeyError:
            pass
        try :
            return self.data[UK_TO_US[key]]
        except KeyError:
            pass
        raise KeyError(key)
    #if the key exist it return it else it check if the key was spelled in British English
    #if it is the case it translated to american and retrieved to underlying dictionary
    def __setitem__(self,key,value):
        try :
            key = UK_TO_US[key] #tries to find the given key in the UK_TO_US dictionary.
        except KeyError:
            pass
        self.data[key] = value

english_spelled = EnglishSpelledDict({"color":"blue","flavour":"vanilla"})
print(english_spelled)
#out: {'color': 'blue', 'flavor': 'vanilla'}
english_spelled2 = EnglishSpelledDict({"colour":"blue","flavour":"vanilla"})
print(english_spelled2)
#out:{'color': 'blue', 'flavor': 'vanilla'}
print(english_spelled2.items())
#out: ItemsView({'color': 'blue', 'flavor': 'vanilla'})
#  here the key colour is switched to color

"""
Custom dictionary that accesses keys through Values
"""
class ValueDict(dict):
    def key_of(self, value):
        for k, v in self.items():
            if v == value:
                return k
        raise ValueError(value)

    def keys_of(self, value):
        for k, v in self.items():
            if v == value:
                yield k

inventory = ValueDict()
inventory["apple"] = 2
inventory["banana"] = 3
inventory.update({"orange": 2})
print(inventory)
#{'apple': 2, 'banana': 3, 'orange': 2}
key_of_2 = inventory.key_of(2)
print(key_of_2)
#apple only the first key is return
list_key = list(inventory.keys_of(2))
print(list_key)
#['apple', 'orange'] # the keys_of return the keys for the selected value 2
