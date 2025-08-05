import os

todoList = []

def load_tasks():
  if os.path.exists("todo.txt"):
    with open("todo.txt", "r") as file:
      for line in file:
        todoList.append(line.strip())

  else:
    with open("todo.txt", "w") as file:
      pass

def save_todolist():
  with open("todo.txt", "w") as file:
    for item in todoList:
      file.write(item)
      file.write("\n")

  print("CLI TodoList Saved!")
  print("\n")  

def add_task():
  while True:
    taskToAdd = input("Mention the task name that you want to add in your CLI TodoList: ").strip()

    if taskToAdd.lower() in [item.lower() for item in todoList]:
      print("Task already exists!")
      continue

    elif taskToAdd:
      todoList.append(taskToAdd)
      print("Task added successfully...")

    else:
      print("You have not entered any task. Try again!") 
      continue 

    continueOperation = input("Want to add more? y/n: ")
    if not (continueOperation.lower() == 'y'):
      break 
  print("\n")  

def delete_task():
  while True:
    taskToDelete = input("Mention the task name that you want to delete from your CLI TodoList: ").strip()
    matched_task = None

    if not taskToDelete:
      print("Enter valid task for deletion!")
      continue

    if taskToDelete.lower() not in [item.lower() for item in todoList]:
      print("Task not found for deletion")

    else:
      for item in todoList:
        if item.lower() == taskToDelete.lower():
          matched_task = item

      if matched_task:
        todoList.remove(matched_task)
        print("Task deleted successfully...")

      else:
        print("Task not Found for deletion")

    continueOperation = input("Want to continue this operation? y/n: ")
    if not (continueOperation.lower() == 'y'):
      break   

  print("\n")  

def view_tasks():
  if not todoList:
    print("There are not tasks to show! Add the tasks now!")

  else:
    print("Tasks currently in your CLI TodoList:")
    for item in todoList:
      print(item)

  print("\n")    

load_tasks()
print("Welcome to CLI TodoList, What tasks you want to perform today!")
print("Note:- Save your Todolist before stopping for persisting your changes!")

while True:
  print("Operations Available:")
  print("1. Add a task")
  print("2. Delete a task")
  print("3. View the tasks")
  print("4. Save TodoList")
  print("5. Stop")

  try:
    taskNumber = int(input("Enter the desired operation number: "))

  except ValueError:
    print("Enter a valid number!")
    print("\n")
    continue

  match (taskNumber):
    case 1:
      add_task()
    case 2:
      delete_task()
    case 3:
      view_tasks() 
    case 4:
      save_todolist()  
    case 5:
      break
    case _:
      print("Enter a valid task number")    

print("Thank you for using TodoList, have a great day!!!")      