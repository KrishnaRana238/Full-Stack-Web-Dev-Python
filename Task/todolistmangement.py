#task1
# you have to create a to do list management system 
#create a list of list of task
#add new task
#mark a task as done by removing it
#show the number of tasks remaining

# Task 1: To-Do List Management System
# Create a list of tasks, add new tasks, mark tasks as done, and show the
# number of tasks remaining.    


def todo_list_management():
    task_list = []
    
    while(True):
        print("\n To Do List Management System")
        print("1. Add a new task")
        print("2. Mark a task as done")
        print("3. Show remaining tasks")
        print("4. Exit")
        
        choice = input("WHat you want to do? (1/2/3/4): ")
        
        if choice == '1':
            task = input("Enter the new task: ")
            task_list.append(task)
            print(f"Task '{task}' added to the list.")
        
        elif choice == '2':
            if len(task_list) == 0:
                print("No tasks to mark as done.")
            else:
                print("Current Tasks:")
                i =0
                while i < len(task_list):
                    print(str(i) + ". " + task_list[i])
                    i += 1
                task_number = input("Enter the index of the task to mark as done: ")

                if task_number.isdigit():  # check BEFORE converting
                    task_index = int(task_number)
                    if 0 <= task_index < len(task_list):
                        done_task = task_list.pop(task_index)
                        print(f"Task '{done_task}' marked as done and removed from the list.")
                    else:
                        print("Invalid task index. Please try again.")
                else:
                    print("Invalid input. Please enter a valid task index.")
                    
                    
        elif choice == '3':
            if len(task_list) == 0:
                print("No tasks remaining.")
            else:
                print("Remaining Tasks:")
                i = 0
                while i < len(task_list):
                    print(str(i) + ". " + task_list[i])
                    i += 1
                print("Toatl task left: ", str(len(task_list)))
        
        elif choice == '4':
            print("Exiting To-Do List Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")

todo_list_management()
     
                    