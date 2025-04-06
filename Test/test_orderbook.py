"""
Orderbook unit test
These unit test are used to test each behavior expected in the project
"""

import sys
import pytest

sys.path +=['../Order_Book']

from classes import Task
from classes import OrderBook

#pytest.fixture avoid repetition inside the test, pass at argument of the test function

@pytest.fixture
def three_tasks():
    orders = OrderBook()
    Task.id_generator_to_zero()#avoid mismatch for the id_key
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    return orders

"""
Test part 1
"""
class TestTaskInstantiation:
    """
    This class test if the instantiation of the Task class works as expected:
    method counter_id_generator_to_zero() force the class counter to 0
    counter is incremented by one each time a new task is created
    a new task is created with the status NOT_FINISHED
    method is_finished switch a task to the FINISHED status
    """
    def test_counter_id_generator_to_zero(self):
        t1 = Task("program hello world", "Eric", 3)
        Task.id_generator_to_zero()
        assert Task.number_of_tasks() == 0
    def test_counter_one_task(self):
        Task.id_generator_to_zero()
        t1 = Task("program orderbook", "victor", 15)
        assert Task.number_of_tasks() == 1
    def test_counter_two_tasks(self):
        Task.id_generator_to_zero()
        t1 = Task("program orderbook", "victor", 15)
        t2 = Task("program test file for orderbook", "victor", 3)
        assert Task.number_of_tasks() == 2
    # "A task cannot be finished when it is created"
    def test_is_finished(self):
        t1 = Task("program hello world", "Eric", 3)
        assert t1.is_finished() is not True
    def test_print_is_not_finished(self):
        t1 = Task("program hello world", "Eric", 3)
        t1.mark_finished()
        assert t1.is_finished() is True

class TestTaskPrint:
    """
    Test print behavior of Task class as expected in part one
    """
    def test_task_print_attributes(self,capsys,monkeypatch):
        t1 = Task("program hello world","Eric",3) #create first instance part 1
        monkeypatch.setattr(t1,"_Task__id_number", 1)
        print(t1.id,t1.description,t1.programmer,t1.workload)
        output = capsys.readouterr() #get the output of the print above
        assert output.out == str(t1.id) + " program hello world Eric 3\n" #print auto create \n newline

    def test_print_task(self,monkeypatch):
        t1 = Task("program hello world", "Eric", 3)
        monkeypatch.setattr(t1,"_Task__id_number",1)
        monkeypatch.setattr(t1,"_Task__done_status","NOT FINISHED")
        assert str(t1) == "1: program hello world (3 hours), programmer Eric NOT FINISHED"

#The state of a task (finished or not finished) can be checked with a function that returns a
#Boolean value
def test_is_finished_return_boolean():
    t1 = Task("program hello world", "Eric", 3)
    assert type(bool(t1.is_finished())) == bool

"""
Test part 2
"""
class TestOrderBookAddOrder:

    #test if the add_order method fill correctly the dictionary
    def test_add_order(self,three_tasks):
        orders_in_dict = len(three_tasks.order_dictionary.items())
        assert orders_in_dict == 3
        three_tasks.add_order("program webstore", "Adele", 10)
        assert len(three_tasks.order_dictionary.items()) == orders_in_dict + 1

    #test if the add_order method fill correctly the list of not finished tasks
    def test_add_order_not_finished(self,three_tasks):
        order_ids_in_not_finished_list = len(three_tasks.orderID_not_finished)
        assert order_ids_in_not_finished_list == 3
        three_tasks.add_order("program webstore", "Adele", 10)
        assert len(three_tasks.orderID_not_finished) == order_ids_in_not_finished_list + 1
        assert three_tasks.orderID_not_finished == [1,2,3,4]

    #test if the add_order method fill correctly the list of programmers
    def test_add_new_programmer(self,three_tasks):
        programmers = three_tasks.order_dictionary_programmer.keys()
        assert list(programmers) == ["Adele", "Eric"]
        three_tasks.add_order("program webstore", "Adele", 10)
        assert len(three_tasks.order_dictionary_programmer.items()) == 2
        three_tasks.add_order("program webstore", "Anna", 10)
        assert list(programmers) == ["Adele", "Eric","Anna"]


class TestOrderPrint:
    def test_order_book_print_all_order(self,capsys,three_tasks):
        for order in three_tasks.all_orders():
            print(order)
        capture_print_output = capsys.readouterr()
        assert (capture_print_output.out ==
            ("1: program webstore (10 hours), programmer Adele NOT FINISHED\n"
            "2: program mobile app for workload accounting (25 hours), programmer Eric NOT FINISHED\n"
            "3: program app for practising mathematics (100 hours), programmer Adele NOT FINISHED\n"))

    def test_order_book_print_all_unique_programmer(self,capsys,three_tasks):
        for programmer in three_tasks.programmer():
            print(programmer)
        capture_print_output = capsys.readouterr()
        assert (capture_print_output.out ==
            ("Adele\n"
             "Eric\n"))

"""
Test part 3
"""
#TODO: add test for part 6

"""
Test part 4
"""
def test_order_book_mark_finished_not_finished(capsys,three_tasks):
    three_tasks.mark_finished(1)
    three_tasks.mark_finished(2)
    for order in three_tasks.all_orders():
        print(order)
    capture_print_output = capsys.readouterr()
    assert (capture_print_output.out ==(
        "1: program webstore (10 hours), programmer Adele FINISHED\n"
        "2: program mobile app for workload accounting (25 hours), programmer Eric FINISHED\n"
        "3: program app for practising mathematics (100 hours), programmer Adele NOT FINISHED\n")
                  )

"""
Test part 5
"""
def test_status_of_programmer(three_tasks):

    assert three_tasks.status_of_programmer("Adele") == (0,2,0,110)
    assert three_tasks.status_of_programmer("Eric") == (0,1,0,25)
    three_tasks.mark_finished(1)
    three_tasks.mark_finished(2)
    assert three_tasks.status_of_programmer("Adele") == (1,1,10,100)
    assert three_tasks.status_of_programmer("Eric") == (1,0, 25,0)


