def input_from_console():
    """
    Reads text input from the console.

    Returns:
        str: The text entered by the user.
    """
    return input("Enter text: ")


def read_file_builtin(file_path):
    """
    Reads text from a file using Python's built-in functions.

    Parameters:
        file_path (str): The path to the file.

    Returns:
        str: The contents of the file, or an error message.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {e}"


def read_file_pandas(file_path):
    """
    Reads data from a file using the pandas library.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        str: A string representation of the data, or an error message.
    """
    import pandas as pd
    try:
        df = pd.read_csv(file_path)
        return df.to_string()
    except Exception as e:
        return f"Error reading file with pandas: {e}"