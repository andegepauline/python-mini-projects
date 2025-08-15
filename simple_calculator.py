while True:   #This is used to allow the calculator to keep running, so the user can perform multiple operations without restarting the program.
    print("\n--- Simple Calculator ---")
    
    # Ask user to enter the first number or type 'exit' to quit
    num1_input = input("Enter the first number (or type 'exit' to quit): ")
    if num1_input.lower() == 'exit':
        print("Goodbye!")
        break  # Exit the loop
    
    # Try to convert the input to a float
    try:
        num1 = int(num1_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue  # Restart the loop
    
    # Ask for the second number
    num2_input = input("Enter the second number: ")
    try:
        num2 = int(num2_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Ask the user to choose an operation
    operator = input("Choose an operation (+, -, *, /): ")
    
    # Perform the operation based on user input
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        # Handle division by zero
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            continue
        result = num1 / num2
    else:
        print("Invalid operator. Please choose one of +, -, *, /.")
        continue
    
    # Show the result
    print(f"Result: {num1} {operator} {num2} = float{result}")
