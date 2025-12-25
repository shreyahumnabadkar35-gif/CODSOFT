
tasks=[]
while True:
    print("\n---- To Do List-----")
    print("1.Add Tasks")
    print("2.Show tasks")
    print("3.Update tasks")
    print("4.complete tasks")
    print("5.Exit")

    ch=input("Enter your choice:")

    if ch == '1':
        t=input("Enter new task:")
        tasks.append({"name":t,"status":"pending"})
        print("Task added successfully")

    elif ch=='2':
        if len(tasks)==0:
            print("No tasks available")
        else:
            for i in range(len(tasks)):
                print(i+1," . ",tasks[i]["name"],"-",tasks[i]["status"])
    
    elif ch=='3':
        if len(tasks)==0:
            print("No tasks to update")
        else:
            for i in range(len(tasks)):
                print(i+1,".",tasks[i]["name"])

            num=int(input("Enter task no to update:"))
            tasks[num-1]["name"]=input("Enter updated task:")
            print("Task updated")

    elif ch=='4':
        if len(tasks)==0:
            print("No tasks to complete")
        else:
            for i in range(len(tasks)):
                print(i+1,".",tasks[i]["name"])
            
            num=int(input("Enter task no:"))
            tasks[num-1]["status"]="completed"
            print("Task marked as completed")
    
    elif ch=='5':
        print("Closing To Do list")
        break

    else:
        print("You enttered wrong choice,try again")

   
