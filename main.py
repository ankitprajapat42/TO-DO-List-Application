task = []
def add_task():
    n = int(input("\nHow Many Task you will add : "))
    for i in range(n):
        t = input(f"Enter the Task Name {i+1} : ")
        task.append(t)
    print(f"{i+1} Task is Succesfully Added")
    

def update_task():
    t = input("\nWhich Task you will bw update : ")
    if t in task:
        n = task.index(t)
        task.remove(t)
        new_task = input("Enter the New Task : ")
        task.insert(n, new_task)
        print("\nTask Succesfully Update")
    else:
        print("\nThis task is note define in the List")

def delete_task():
    t = input("\nWhich task you delete : ")
    if t in task:
        task.remove(t)
        print("Task is Succesfully Delete")
    else:
        print("This Task is Not Exest in the list")

def veiw_task():
    for i in task:
        print(i)

while True:
    print('\n',"TO-DO List Application".center(40, '*'),'\n')
    print("Press 1 for Add Task\nPress 2 for Delete Task\nPress 3 for Update Task\nPress 4 for View Task\nPress 5 for Exit")
    n = input("Choice : ")
    if n=='1':
        add_task()
    elif n=='2':
        delete_task()
    elif n=='3':
        update_task()
    elif n=='4':
        veiw_task()
    elif n=='5':
        print("Application Close".center(40, '-'))
        break
    else:
        print("please Select the Correct option")



    
