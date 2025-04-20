def guest_book():
    while True:
        # Prompt the user for their name
        name = input("Please enter your name (or type 'quit' to exit): ")
        
        # Check if the user wants to exit
        if name.lower() == 'quit':
            print("Thank you for visiting!")
            break
        
        # Print a greeting
        print(f"Hello, {name}! Welcome!")
        
        # Record the visit in guest_book.txt
        with open('guest_book.txt', 'a') as file:
            file.write(f"{name}\n")  # Write the name followed by a newline

if __name__ == "__main__":
    guest_book()