print("Welcome to Calculator Project")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
option = int(input("Select an option for Basic Calculator Operation : "))

if option == 1:
    n1= int(input("Enter first number : "))
    n2= int(input("Enter second number : "))
    n3= n1+n2
    print("Addition is " + str(n3))
    
elif option== 2:
    n1= int(input("Enter first number : "))
    n2= int(input("Enter second number : "))
    n3= n1-n2
    print("Substraction  is " + str(n3))
        
elif option== 3:
    n1= int(input("Enter first number : "))
    n2= int(input("Enter second number : "))
    n3= n1*n2
    print("Multiplication  is " + str(n3))
    
elif option ==4:
        
    n1= int(input("Enter first number : "))
    n2= int(input("Enter second number : "))
    n3= n1/n2
    print("Division is " + str(n3))
        
       
else:
    print("Invalid input")        