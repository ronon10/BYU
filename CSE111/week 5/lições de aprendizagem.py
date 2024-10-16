# Example 2
import csv
def main():
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open("C:/Users/realves/Documents/BYU/CSE111/week 5/hymns.csv", "rt") as csv_file:
        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)
        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:
            print(row_list)
# Call main to start this program.
if __name__ == "__main__":
    main()

print()


# Example 1
def main():
    # Read the contents of a text file
    # named plants.txt into a list.
    text_list = read_list("C:/Users/realves/Documents/BYU/CSE111/week 5/plants.txt")
    # Print the entire list.
    print(text_list)
def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.
    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list that will store
    # the lines of text from the text file.
    text_list = []
    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:
        # Read the contents of the text
        # file one line at a time.
        for line in text_file:
            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()
            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)
    # Return the list that contains the lines of text.
    return text_list
# Call main to start this program.
if __name__ == "__main__":
    main()
