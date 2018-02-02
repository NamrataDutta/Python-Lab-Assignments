#Initializing symbols list
Symbol =['$','@','#','!']


while True :
 passwcheck = input("Enter the password :")

#calculating the length of the entered password and checking the conditions
 if len(passwcheck)< 6 :
    print("The length of the password should be at least 6 characters long")
    continue
 elif len(passwcheck)> 16 :
    print("The length of the password should be not be greater than 16")
    continue

 #checking for any numbers in the password entered
 elif not any(char.isdigit() for char in passwcheck):
    print('The password should have at least one numeral')
    continue
 #checking for Upper case letters entered
 elif not any(char.isupper() for char in passwcheck):
    print('The password should have at least one uppercase letter')
    continue
 #checking for lower case letter entered
 elif not any(char.islower() for char in passwcheck):
    print('The password should have at least one lowercase letter')
    continue
 #checking for presence of special characters in the password entered from the list declared above
 elif not any(char in Symbol for char in passwcheck):
    print('The password should have at least one of the symbols $@#!')
    continue
 #If every condition matches, then the loop will stop and the below statement will be printed
 else :
    print("Password entered is correct")
    print(passwcheck)
    break

