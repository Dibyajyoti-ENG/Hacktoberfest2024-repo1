def to_do_list():
    tasks=[]
    print("------WELCOME TO THE TO-DO LIST APP------")

    total_task=int(input("Enter how many task you want to add = "))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task {i} = ")
        tasks.append(task_name)
    
    print("Today's tasks are\n",*tasks)

    while True:
        print("If you want to update something in the To-Do List please choice the given option accordingly")
        operation = int(input("1:- ADD SOME MORE TASK\n2:- UPDATE ANY TASK\n3:- DELETE ANY TASK\n4:- VIEW THE UPDATES\n5:- EXIT THE TO-DO LIST APP"))
        
        if operation==1:
            add=input("Enter the new task to be added in the To-Do List = ")
            if add in tasks:
                print(add,'task is already in the To-Do List')
            else :
                tasks.append(add)
                print(f'The {add} task is added successfully added to the To-Do List')
        
        elif operation==2:
            updated_task = input("Enter the name of the task to updated in the To-Do List = ")
            up=input(f"Enter The new task that is to updated in place of {updated_task}")
            if updated_task in tasks:
                ind=tasks.index(updated_task)
                tasks[ind]=up
                print(f'The {up} task is updated successfully to the To-Do List')
        
        elif operation==3:
            deleted_task=input("Enter the name of the task to be deleted from the To-Do List")
            if deleted_task in tasks:
                ind=tasks.index(deleted_task)
                del tasks[ind]
                print(f'The {deleted_task} task is successfully deleted from the To-Do List')

        elif operation==4:
            print("The Updated To-Do List:/n",*tasks)

        elif operation==5:
            print("Closing The To-Do List ........")
            break

        else :
            print("Invalid Choice")

to_do_list()