def choice_1(N):
    fib_series = []
    a, b = 0, 1
    for _ in range(N):
        fib_series.append(a)
        temp=a
        a=b
        b=temp+b
    return fib_series

def choice_2(max_value):
    fib_series = []
    a, b = 0, 1
    while a <= max_value:
        fib_series.append(a)
        temp=a
        a=b
        b=temp+b
    return fib_series

while True:
    print("\nChoose an option: ")
    print("1. Generate Fibonacci series by number of terms")
    print("2. Generate Fibonacci series by maximum value")
    print("3. Exit")
    
    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        continue
    
    if choice == 1:
        try:
            N = int(input("Enter the number of terms: "))
            if N <= 0:
                print("Please enter a positive number.")
            else:
                series = choice_1(N)
                print("Fibonacci series (up to", N, "):", *series, seperate=", ")

        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    elif choice == 2:
        try:
            max_value = int(input("Enter the maximum value: "))
            if max_value < 0:
                print("Please enter a non-negative number.")
            else:
                series = choice_2(max_value)
                print("Fibonacci series (up to", max_value, "):", *series, seperate=", ")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    elif choice == 3:
        print("GoodLuck")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 3.")
