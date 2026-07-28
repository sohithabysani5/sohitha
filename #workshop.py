#workshop
back_stack= []
forward_stack= []
while True:
    print("\n==== Browser History Manager ====")
    print("1. Visit a new page")
    print("2. Back")
    print("3. Forward")
    print("4.Display History")
    print("5. Display Current Page")
    print("6. Exit")
    choice= int(input("Enter your choice: "))
    if choice==1:
        page= input("Enter pagename: ")
        back_stack.append(page)
        current_page= page
        forward_stack.clear()
        print("Visited:", page)
    elif choice==2:
        if len(back_stack)==0:#if there no more pages in the history
            print("No pages in history to go back to.")
        else:
            forward_stack.append(current_page)
            current_page= back_stack.pop()
            print("Moved back to ", current_page)
    elif choice==3:
        if len(forward_stack)==0:
            print("no pages in history to go to back")
        else:
            back_stack.append(current_page)
            current_page=forward_stack.pop()
            print("Forwarded to ", current_page)
    elif choice==4:
        print("Current page: ", current_page)
    elif choice==5:
        print("\nBack Sytack :",back_stack)
        print("Current page: ",current_page)
        print("Forward stack: ", forward_stack)
    elif choice==6:
        print("Browser Closed!!!")
    else:
        print("Invalid Choice .")
    

        

