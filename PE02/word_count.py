def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the contents of the file
            contents = file.read()
            # Split the contents into words
            words = contents.split()
            # Count the number of words
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Prompt the user for the file path
    file_path = input("Enter the path to the text file: ")
    word_count = count_words_in_file(file_path)
    
    if word_count is not None:
        print(f"The number of words in the file is: {word_count}")