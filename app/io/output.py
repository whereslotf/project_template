def print_to_console(text):
    """
    Prints the given text to the console.

    Parameters:
        text (str): The text to print.
    """
    print(text)


def write_to_file(file_path, text):
    """
    Writes the given text to a file using Python's built-in functions.

    Parameters:
        file_path (str): The path to the file.
        text (str): The text to write.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)
    except Exception as e:
        print(f"Error writing to file: {e}")


def output_to_console_and_file(text, file_path):
    """
    Outputs the given text to the console and writes it to a file.

    Parameters:
        text (str): The text to output.
        file_path (str): The path to the file.
    """
    print_to_console(text)
    write_to_file(file_path, text)