import sys
import time
from classes import OrderBook,Task

#TODO: add comments
#TODO: look if need to handle other errors
#TODO: add part to save the orderbook in jason or other method (add a sub command)
#TODO: add part to download an orderbook (and update in all dictionary)
#TODO: recheck all test
#TODO: recheck all test
if __name__ == "__main__":
    orders = OrderBook() #instantiation of the order book
    Task.id_generator_to_zero() #with a counter force to 0 if orders already created in class.py
    while True: #initiate a loop while true : message with the commands will be print after each user's operations
        print(
        "******* Main_commands ********\n"
        "0 - Quit\n"
        "1 - Add order\n"
        "2 - list finished tasks\n"
        "3 - list unfinished tasks\n"
        "4 - mark task as finished\n"
        "5 - programmers\n"
        "6 - status of programmer\n"
        "******************************"
        )
        command = input("command: ") #user input for the command
        if command == "0":
            confirm_quit = input("Are you sure you want to quit? (Y/n)")
            if confirm_quit == 'Y':
                print("quitting")
                time.sleep(1) #time.sleep added for each output to let user time to see the answer
                sys.exit()
        #for each input, a try except block is added to avoid errors
        elif command == "1":
            description = input("description: ")
            try:
                programmer, workload = input("programmer and workload estimate: ").split(" ")
            except ValueError:
                print("erroneous input")
                time.sleep(1)
            else:
                try:
                    workload = int(workload)
                except ValueError:
                    print("erroneous input")
                    time.sleep(1)
                else:
                    try:
                        orders.add_order(description, programmer, workload)
                    except ValueError:
                        print("erroneous input")
                    else:
                        print("added!")
                        time.sleep(2)


        elif command == "2":
            if len(orders.orderID_finished) == 0:
                print("no finished tasks")
                time.sleep(2)
            else :
                finished_tasks = [orders.order_dictionary[id_num] for id_num in orders.orderID_finished]
                for order in finished_tasks:
                    print(order)
                time.sleep(2)
        elif command == "3":
            if len(orders.orderID_finished) == 0:
                for order in orders.all_orders():
                    print(order)
                time.sleep(2)
            else:
                not_finished_tasks = [orders.order_dictionary[id_num] for id_num in orders.orderID_not_finished]
                for order in not_finished_tasks:
                    print(order )
                time.sleep(2)

        elif command == "4":
            try:
                id_num = int(input("id: "))
            except ValueError:
                print("erroneous input")
                time.sleep(1)
            else:
                try:
                    orders.mark_finished(id_num)
                except KeyError:
                    print("erroneous input")
                    time.sleep(1)
                else:
                    print("marked as finished")
                    time.sleep(2)
        elif command == "5":
            for programmer in orders.programmer():
                print(programmer)
            time.sleep(2)
        else :
            if command == "6":
                programmer = input("programmer: ")
                try:
                    status = orders.status_of_programmer(programmer)
                except (KeyError,ValueError,NameError):
                    print("erroneous input")
                    time.sleep(1)
                else:
                    print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]} ")
                    time.sleep(2)
