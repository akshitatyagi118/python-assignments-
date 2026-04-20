
def read_file():
    # Everything inside the function must be indented
    filename = input("Enter the filename: ")

    try:
        # Try to open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            print(content) # Don't forget to print the content!

    except FileNotFoundError:
        print("Error: The file does not exist.")

    except PermissionError:
        # Fixed the missing quote and parenthesis here
        print("Error: You do not have permission to read this file.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function at the very end (no indentation)
read_file()

