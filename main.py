def main():
    """
    Main function that calls input functions to get text from various sources,
    then prints the results to the console and writes them to a file.
    """
    from app.io.input import input_from_console, read_file_builtin, read_file_pandas
    from app.io.output import print_to_console, write_to_file, output_to_console_and_file

    console_text = input_from_console()

    builtin_text = read_file_builtin("data/example.txt")

    pandas_text = read_file_pandas("data/example.csv")

    combined_text = (
        "Console Input: " + console_text + "\n" +
        "Built-in File Read: " + builtin_text + "\n" +
        "Pandas File Read: " + pandas_text + "\n"
    )

    output_to_console_and_file(combined_text, "output.txt")


if __name__ == "__main__":
    main()
