# Program: Read a file and write a modified version to a new file

def modify_content(content):
    """
    Modify the file content.
    For this example, we'll convert everything to uppercase.
    You can replace this with any custom modification.
    """
    return content.upper()


def main():
    filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify content
        modified = modify_content(content)

        # Create new filename
        new_filename = "modified_" + filename

        # Write modified content into new file
        with open(new_filename, "w") as new_file:
            new_file.write(modified)

        print(f"Modified file has been saved as: {new_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
# Program: Read a file and write a modified version to a new file

def modify_content(content):
    """
    Modify the file content.
    For this example, we'll convert everything to uppercase.
    You can replace this with any custom modification.
    """
    return content.upper()


def main():
    filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify content
        modified = modify_content(content)

        # Create new filename
        new_filename = "modified_" + filename

        # Write modified content into new file
        with open(new_filename, "w") as new_file:
            new_file.write(modified)

        print(f"Modified file has been saved as: {new_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
