def add_numbers():
    try:
        # Prompt for the first number
        num1 = input("Enter the first number: ")
        # Convert the first input to an integer
        num1 = int(num1)

        # Prompt for the second number
        num2 = input("Enter the second number: ")
        # Convert the second input to an integer
        num2 = int(num2)

        # Calculate the sum
        result = num1 + num2
        print(f"The result of adding {num1} and {num2} is: {result}")

    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Error: Please enter valid numbers.")

# Example usage
if __name__ == "__main__":
    add_numbers()