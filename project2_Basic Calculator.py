
"""
Example Output:

=== Basic Calculator ===
1. Add
2. Subtract
3. Multiply
4. Divide

Choose an option: 1
Enter first number: 12
Enter second number: 8
Result: 20.0
"""



print("=== Basic Calculator ===")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

input_option = input("Choose an option: ").strip()
result = None

if input_option in ["1", "2", "3", "4"]:
    first_number = float(input("Enter first number: ").strip())
    second_number = float(input("Enter second number: ").strip())

    if input_option == "1":
        result = first_number + second_number
    elif input_option == "2":
        result = first_number - second_number
    elif input_option == "3":
        result = first_number * second_number
    elif input_option == "4":
        if second_number != 0:
            result = first_number / second_number
        else:
            print("Error: Division by zero is not allowed.")

    if result is not None:
        print(f"Result: {result}")
else:
    print("Invalid option selected. Please choose a valid option (1-4).")
