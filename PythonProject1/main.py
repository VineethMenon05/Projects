todos = []

while True:                                                                #This will be true every time if we use false without any statements the code will not run at all
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':                                                        #Cases are used to add the different sections on the code
            todo = input("Enter a todo: ") + "\n"
            with open('todos.txt', 'r') as file:                           #This will save the data which will be provided in txt file
                todos = file.readlines()
            todos.append(todo)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
                file.close()

                new_todos = []
                for item in todos:
                    new_item = item.strip('\n')                             #This is to remove the extra /n line from the list
                    new_todos.append(new_item)
                for index, item in enumerate(new_todos):
                    row = f"{index + 1}-{item}"
                    print(row)

        case 'edit':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            number = int(input("Number of todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            number = int(input("Number of todo to complete: "))
            todos.pop(number - 1)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'exit':                                                          #This case is used to exit the while loop
            break

print("BYE!:)")



