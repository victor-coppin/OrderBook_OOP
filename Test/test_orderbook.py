"""
Orderbook unit test
These unit test are used to test each behavior expected in the project


"""
import pytest
import sys

from IPython.utils.capture import capture_output

sys.path +=['../Order_Book']

from classes import Task

def test_task_print_attributes(capsys):
    t1 = Task("program hello world","Eric",3) #create first instance part 1
    t1.id = 1
    print(t1.id,t1.description,t1.programmer,t1.workload)
    capture_print_output = capsys.readouterr()
    assert capture_print_output.out == str(t1.id) + " program hello world Eric 3\n" #print auto create \n newline








