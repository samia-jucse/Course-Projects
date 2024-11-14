Favourite_Food_List=[]
while True:
    print("\t\tWelcome To Favourite Foods Manager")
    print("\t\t\t 1. Add Foods")
    print("\t\t\t 2. Remove Foods")
    print("\t\t\t 3. View All Favourite Foods.")
    print("\t\t\t 0. Exit")
    
    try:
        option = int(input("Choose an Option: "))
    except  ValueError :
        print("Invalid Input!Please Enter a Valid Number") 
        print("\n")
        continue 
    
    
    if option==1:
        food_name = input("Enter Favourite Food Name:")
        food =food_name.capitalize()
        Favourite_Food_List.append(food)
        print(f"{food} Added Sucessfully!")
        print(Favourite_Food_List)
        print("\n")
        
    elif option ==2:
        food_name = input("Enter Favourite Food Name For Remove :")
        food =food_name.capitalize()
        try:
             Favourite_Food_List.remove(food)
             print(f"{food} Remove Successfully")
             print(Favourite_Food_List)
        except ValueError:  
             print(f"{food} is not in the Favourite Food List, Please Check the List")   
             print(Favourite_Food_List)
             print("\n")
    
    elif option==3:
        if Favourite_Food_List:
           print("Your Favourite Foods: ")
           for _, food in enumerate (Favourite_Food_List,start=1) :
             print(f"_.{food}") 
        else:
            print("Food List is empty or did not added yet! ")      
            print("\n")     
            
    elif option ==0:
        print("thanks For Using Favourite Foods Manager ")
        break
    else:
        print("Invalid Choice!, Please Enter Again")
        print("\n")        