"""
Orderbook unit test
These unit test are used to test each behavior expected in the project
"""

import sys

sys.path +=['../Order_Book']

from classes import Task

def test_task_print_attributes(capsys):
    """
    will test the printing of attributes
    we set the t1.id to 1 to avoid missmatch if t1 is not the first task
    capsys (from pytest) allow to capture stdout i.e the print display and compare it with the expected output
    capture_print_output.out : .out is used to just return the output
    """
    t1 = Task("program hello world","Eric",3) #create first instance part 1
    t1.id = 1
    print(t1.id,t1.description,t1.programmer,t1.workload)
    capture_print_output = capsys.readouterr()
    assert capture_print_output.out == str(t1.id) + " program hello world Eric 3\n" #print auto create \n newline

def test_print_task():
    t1 = Task("program hello world", "Eric", 3)
    t1.id = 1
    t1.mark_not_finished()
    assert str(t1) == "1: program hello world (3 hours), programmer Eric NOT FINISHED"

def test_print_is_finished():
    t1 = Task("program hello world", "Eric", 3)
    t1.mark_not_finished()
    assert t1.is_finished() is not True

def test_print_is_not_finished():
    t1 = Task("program hello world", "Eric", 3)
    t1.mark_finished()
    assert t1.is_finished() is True



