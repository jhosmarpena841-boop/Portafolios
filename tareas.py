# tareas.py - Simple To-Do List manager
# Author: jhosmar
# Date: 2026-04-05
#
# What it does:
# - Add new tasks
# - View all tasks
# - Mark tasks as completed
# - Delete tasks
# - Tasks persist between sessions using a text file
#
# How to use:
# Run: python tareas.py
# Then choose from menu:
#   1. View tasks
#   2. Add task
#   3. Complete task
#   4. Delete task
#   5. Exit

import time

try:
    with open("tareas.txt", "r") as f:
        tareas = [linea.strip() for linea in f]
except:
    tareas = []

while True:
    print ("To-do list")
    print ("1. view tasks")
    print ("2. add task")
    print ("3. complete task")
    print ("4. delete task")
    print ("5. exit")
    option = input("Enter your option: ")
    if option == "1":
        if len(tareas) == 0:
            print ("no tasks")
        else:
            for i, tarea in enumerate(tareas):
                print (f" {i+1}. {tarea}.")
        time.sleep(7)

    elif option == "2":
        nueva_tarea = input("Enter the new task here:")
        tareas.append(nueva_tarea)
        print ("Adding task...")
        with open("tareas.txt", "w") as f:
            for tarea in tareas:
                f.write(tarea+ "\n")
                time.sleep(3)


    elif option == "3":
        for i, tarea in enumerate(tareas):
            print (f"{i+1}. {tarea}")
        num = int(input("Enter the number of the task to delete : "))
        tareas[num-1] = "[X] " + tareas[num-1]
        print ("marking task as completed...")
        with open("tareas.txt", "w") as f:
            for tarea in tareas:
                f.write(tarea+ "\n")
                time.sleep(2)
    elif option == "4":
        for i, tarea in enumerate(tareas):
            print (f"{i+1}. {tarea}.")
        num = int(input("Enter the number of the task to delete  : "))
        eliminada = tareas.pop(num-1)
        print (f"removing. {eliminada}")
        with open("tareas.txt", "w") as f:
            for tarea in tareas:
                f.write(tarea+ "\n")
                time.sleep(2)

    elif option == "5":
        print ("see you later")
        break
    else:
        print ("Invalid option ")
