import sys
import time
from classes import OrderBook,Task

if __name__ == "__main__":
    orders = OrderBook()
    Task.id_generator_to_zero()
    while True:
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
        if command == "0":
            confirm_quit = input("Are you sure you want to quit? (Y/n)")
            if confirm_quit == 'Y':
                print("quitting")
                time.sleep(1)
                sys.exit()

        elif command == "1":
            description = input("description: ")
            programmer,workload = input("programmer and workload estimate: ").split(" ")
            workload = int(workload)
            orders.add_order(description, programmer, workload)
            print("added!")
            time.sleep(2)
            # add_other = input("do you want to continue to add another order? (Y/n)")
            # if add_other == 'Y':

        elif command == "2":
            if len(orders.orderID_finished) == 0:
                print("no finished tasks")
                time.sleep(2)
            else :
                finished_tasks = [orders.order_dictionary[id_num] for id_num in orders.orderID_finished]
                for order in finished_tasks:
                    print(order)

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
            id_num = int(input("id: "))
            orders.mark_finished(id_num)
            print("marked as finished")
            time.sleep(2)
        elif command == "5":
            for programmer in orders.programmer():
                print(programmer)
                time.sleep(2)
        else :
            if command == "6":
                programmer = input("programmer: ")
                status = orders.status_of_programmer(programmer)
                print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]} ")
                time.sleep(2)
