import sys
import time
from classes import OrderBook,Task

#TODO: recheck all test
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
        "******************************"
        )
        command = input("command: ")
        try:
            int(command) in [1, 2, 3, 4, 5, 6]
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
                description = input("description: ")
                try:
                    Task(description,"victor",30)
                except ValueError:
                    print("erroneous input")
                    time.sleep(2)
                else:
                    try:
                        programmer, workload = input("programmer and workload estimate: ").split(" ")
                        orders.add_order(description, programmer, workload)
                        print("added!")
                        time.sleep(2)
                    except Exception:
                        print("erroneous input")
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
                except KeyError:
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

