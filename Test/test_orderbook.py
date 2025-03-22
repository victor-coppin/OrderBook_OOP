"""
Orderbook unit test
These unit test are used to test each behavior expected in the project
"""

import sys

from jedi.common import monkeypatch

sys.path +=['../Order_Book']

from classes import Task

def test_task_print_attributes(capsys,monkeypatch):
    """
    Print TEST
    we set the t1.id to 1 to avoid missmatch if t1 is not the first task
    capsys (from pytest) allow to capture stdout,i.e. the print display and compare it
    with the expected output capture_print_output.out :.out is used to just return the output
    ************************************************************************************
    MONKEYPATCH
    Improvement: use the monkeypatch fixture to avoid create an id setter and a mark_not_finish method.
    Code before improvement :
    def test_print_is_finished():
    t1 = Task("program hello world", "Eric", 3)
    t1.mark_not_finished()
    assert t1.is_finished() is not True
    """
    t1 = Task("program hello world","Eric",3) #create first instance part 1
    monkeypatch.setattr(t1,"_Task__id", 1)
    print(t1.id,t1.description,t1.programmer,t1.workload)
    capture_print_output = capsys.readouterr()
    assert capture_print_output.out == str(t1.id) + " program hello world Eric 3\n" #print auto create \n newline

def test_print_task(monkeypatch):
    t1 = Task("program hello world", "Eric", 3)
    monkeypatch.setattr(t1,"_Task__id",1)
    monkeypatch.setattr(t1,"_Task__done_status","Not Finished")
    assert str(t1) == "1: program hello world (3 hours), programmer Eric NOT FINISHED"

def test_print_is_finished(monkeypatch):
    t1 = Task("program hello world", "Eric", 3)
    monkeypatch.setattr(t1,"_Task__done_status","Not FINISHED")
    assert t1.is_finished() is not True

def test_print_is_not_finished():
    t1 = Task("program hello world", "Eric", 3)
    t1.mark_finished()
    assert t1.is_finished() is True



