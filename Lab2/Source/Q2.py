Contact_list=[{"name":"Namrata","number":"8167234564","email":"namratadutta4@gmail.com"},{"name":"Pujita","number":"1414244141","email":"pujitam212@gmail.com"}]
while True:
    print("a) Display contact by name")
    print("b) Display contact by number")
    print("c) Edit contact by name")
    print("d) Exit")

    choice=str(input("Enter your choice from above: "))

    if choice=='a':
        input1=(input("Enter the name: "))
        print(next(item for item in Contact_list if item["name"]==input1))
    elif choice=='b':
        input2=(input("Enter the number: "))
        print(next(item for item in Contact_list if item["number"]==input2))
    elif choice=='c':
        input3=input("Enter the contact name you want to edit: ")
        for item in Contact_list:
            if item["name"]==input3:
                item["number"]=input("Enter the new contact number: ")
        print(Contact_list)
    elif choice=='d':
        break
