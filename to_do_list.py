
print("Welcome to your To-Do-List!")
todo_list = []  # Empty list for tasks 

while True:
    print("\nWhat would you like to do?")
    print("1 - Add a task")
    print("2 - Show tasks")
    print("3 - Complete a task")
    print("4 - Exit program")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Which task should be added? ")
        todo_list.append(task)
        print(f"'{task}' has been added.")

    elif choice == "2":
        if len(todo_list) == 0:
            print("No tasks available.")
        else:
            print("Your tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(todo_list) == 0:
            print("No tasks to complete.")
        else:
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
            num = int(input("Which task is completed? (Enter number): "))
            if 1 <= num <= len(todo_list):
                completed = todo_list.pop(num - 1)
                print(f"'{completed}' has been removed.")
            else:
                print("Invalid number.")

    elif choice == "4":
        print("Program ended. See you soon!")
        break

    else:
        print("Invalid input, please try again.")

