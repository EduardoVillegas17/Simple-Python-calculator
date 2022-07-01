#Imports



#globals




#functions
from re import I
from unittest import result


def print_menu():
    print("----------------")
    print("   PyCal 3000   ")
    print("----------------")

    print("[1] Sum")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Division")
    print("[x] Exit")



#Plain instructions
option=""
while option!="x":

    print_menu()
    option = input ("Please select an option:")
    if option=="x":
        break#end the loop


    #ask for the 2 num
    num1=float(input("Please provide num1: "))
    num2=float(input("Please provide num2: "))
    if option == "1":
        result= num1+num2

    elif option == "2":
        result= num1-num2

    elif option == "3":
        result= num1*num2

    elif option == "4":
        if num2 == 0:
            
            result="Error!! the second number is zero!"
        else:
            result= num1/num2
        
        
    print("The result is: "+ str(result))
    input("Press enter to continue...")
    print("")
    print("")
    print("")
    
print("Thanks for using this software.")

