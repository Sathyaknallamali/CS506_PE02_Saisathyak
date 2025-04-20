def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
            print(f"Contents of {file_name}:")
            print(contents)
    except FileNotFoundError:
        print(f"Sorry, the file '{file_name}' was not found.")

if __name__ == "__main__":
    # List of files to read
    files_to_read = ['cats.txt', 'dogs.txt']
    
    for file_name in files_to_read:
        read_file(file_name)