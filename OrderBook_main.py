import sys
import os
import time
from classes import OrderBook,Task
import pickle

#TODO: recheck all test
if __name__ == "__main__":
    orders = OrderBook() #instantiation of the order book
    Task.id_generator_to_zero() #with a counter force to 0 if orders already created in class.py
    while True:
        #initiate a loop while true : message with the commands will be print after each user's operations
        print(
        "******* Main_commands ********\n"
        "0 - Quit\n"
        "1 - Add order\n"
        "2 - list finished tasks\n"
        "3 - list unfinished tasks\n"
        "4 - mark task as finished\n"
        "5 - programmers\n"
        "6 - status of programmer\n"
        "7 - save orderbook\n"
        "8 - load orderbook\n"
        "******************************"
        )
        command = input("command: ")
        try:
            int(command) in [1, 2, 3, 4, 5, 6, 7, 8]
        except ValueError:
            print("erroneous input")
        else:
            if command == "0":
                confirm_quit = input("Are you sure you want to quit? (Y/n)")
                if confirm_quit == 'Y':
                    print("quitting")
                    time.sleep(2) #time.sleep added for each output to let user time to see the answer
                    sys.exit()

            elif command == "1": #add a new order
                try:
                    description = input("description: ")
                    programmer, workload = input("programmer and workload estimate: ").split(" ")
                    orders.add_order(description, programmer, workload)
                except (ValueError,TypeError,AttributeError):
                    print("erroneous input") #will overload the long erroneous error from Task
                    time.sleep(2)
                else:
                    print("added!")
                    time.sleep(2)
            #list finished tasks
            elif command == "2":
                orders.list_task_finished()
                time.sleep(2)
            #list not finished tasks
            elif command == "3":
                orders.list_task_not_finished()
                time.sleep(2)
            #mark task as finished
            elif command == "4":
                try:
                    id_num = int(input("id: "))
                    orders.mark_finished(id_num)
                    print("marked as finished")
                    time.sleep(2)
                except (ValueError,KeyError):
                    print("erroneous input")
                    time.sleep(2)
            #print the programmers
            elif command == "5":
                for programmer in orders.programmer():
                    print(programmer)
                time.sleep(2)
            #for a given programmer return a tuple showing the workloads finished
            elif command == "6":
                programmer = input("programmer: ")
                try:
                    status = orders.status_of_programmer(programmer)
                    print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]} ")
                    time.sleep(2)
                except KeyError:
                    print("Erroneous input")
                    time.sleep(2)
            elif command == "7":
                try:
                    orderbook_backup = "orderbook.pkl"
                    orders.save_orderbook(orderbook_backup) #try pickle to save the object instance
                except Exception:
                    print("erroneous input")
                else:
                    print("saved!")
                    print(os.path.abspath(orderbook_backup))
                    time.sleep(2)
            elif command == "8":
                try:
                    orderbook_backup = "orderbook.pkl"
                    orders = orders.load_orderbook(orderbook_backup)
                except Exception:
                    print("erroneous input")
                else:
                    print("loaded!")
                    time.sleep(2)


"""
For test
"""
#******** PART 1 ********
# t1 = Task("program hello world","Eric",3)
# print(t1.id,t1.description,t1.programmer,t1.workload)
# print(t1)
# print(t1.is_finished())
# t1.mark_finished()
# print(t1)
# print(t1.is_finished())
# t2 = Task("program webstore","Adele",10)
# t3 = Task("program mobile app for workload accounting","Eric",25)
# print(t2)
# print(t3)
#******** PART 2 ********
# orders = OrderBook()
# orders.add_order("program webstore","Adele",10)
# orders.add_order("program mobile app for workload accounting","Eric",25)
# orders.add_order("program app for practising mathematics","Adele",100)
#
# for order in orders.all_orders():
#     print(order)
#
# print()
#
# for programmer in orders.programmer():
#     print(programmer)
#******** PART 4 ********
# orders = OrderBook()
# orders.add_order("program webstore","Adele",10)
# orders.add_order("program mobile app for workload accounting","Eric",25)
# orders.add_order("program app for practising mathematics","Adele",100)
#
# orders.mark_finished(1)
# orders.mark_finished(2)
#
# for order in orders.all_orders():
#     print(order)
#******** PART 5 ********
# orders = OrderBook()
# orders.add_order("program webstore","Adele",10)
# orders.add_order("program mobile app for workload accounting","Eric",25)
# orders.add_order("program app for practising mathematics","Adele",100)
# orders.add_order("program the next facebook","Eric",1000)
#
# orders.mark_finished(1)
# orders.mark_finished(2)
#
# status = orders.status_of_programmer("Adele")
# print(status)