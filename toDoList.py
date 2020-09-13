# create a to do list with 4 options 1 = add task 2 = delete task 3 = view all tasks q = quit
tasks = {
    
}

task = ""

while task != "q":
    task = input("Press 1 to add task, 2 to delete task, 3 to view tasks, q to quit: ")
    if task == "1":
        tasks[input("Enter a task: ")] = input("Enter the priority (high, medium, low): ")
    elif task == "2":
        print(tasks)
        del tasks[input("Enter task name: ")]
    else:
        print(tasks)

        

                

