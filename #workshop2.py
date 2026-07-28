#workshop2
#ticket management
from queue import Queue
tickets= Queue()
while True:
    print("\n Customer Support Ticket system ")
    print("1. Raise New Ticket")
    print("2. Resolve Ticket")
    print("3. View Next Ticket")
    print("4. Display All Tickets")
    print("5. Count Tickets")
    print("6. Exit")
    choice= int(input("Enter your Choice:"))
    if choice==1:
        ticket_id=input("Enter Ticket ID:")
        customer= input("Enter customer Name:")
        issue= input("Enter Reason: ")
        tickets.put((ticket_id, customer, issue))
        print("Ticket Raised Successfully ! ")
    elif choice==2:
        if tickets.empty():
            print("No tickets available...")
        else:
            resolved= tickets.get()
            print("Ticket_ID:",resolved[0])
            print("Customer:",resolved[1])
            print("Issue:", resolved[2])
    elif choice==3:
        if tickets.empty():
            print("No tickets available...")
        else:
            next_ticket= tickets.queue[0]
            print("\nNext Ticket:")
            print("Ticket_ID:",next_ticket[0])
            print("Customer:",next_ticket[1])
            print("Issue:", next_ticket[2])
    elif choice==4:
        if  tickets.empty():
            print("No Tickets available...")
        else:
            print("\npending Tickets")
            for ticket in list(tickets.queue):
            print("Ticket_ID:", ticket[0])
            print("Customer:", ticket[1])
            print("Issue:", ticket[2])
    elif choice==5:
        print("total Pending Tickets:", tickets.qsize())
    elif choice ==6
         print("Support System Closed!")
         break
    else:
        print("invalid input")



