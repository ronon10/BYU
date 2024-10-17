import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """
    Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
            
    Return:
        A compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                key = row[key_column_index]  # Use the correct column as the key
                dictionary[key] = row  # Store the entire row as the value
    except FileNotFoundError as e:
        print("Error: Missing file")
        print(e)
        return None
    except PermissionError as e:
        print("Error: You don't have permission to read the file.")
        print(e)
        return None
    
    return dictionary

def main():
    # Store details
    store_name = "Inkom Emporium"
    
    try:
        # Read the products.csv file into a dictionary
        products_dict = read_dictionary('C:/Users/realves/Documents/BYU/CSE111/week 5/products.csv', 0)
        if products_dict is None:
            return  # Exit the program if the products file cannot be read
        
        # Initialize variables for calculating the subtotal
        subtotal = 0
        sales_tax_rate = 0.06  # Sales tax of 6%
        total_items = 0  # Track the number of items
        
        # Open and read the request.csv file
        with open('C:/Users/realves/Documents/BYU/CSE111/week 5/request.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            
            print(f"\n{store_name}")
            print("Purchased items:")
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])
                total_items += quantity
                
                # Try to find the product in the dictionary
                try:
                    product_info = products_dict[product_number]
                    product_name = product_info[1]
                    product_price = float(product_info[2])
                    
                    # Calculate the subtotal for this item
                    item_total = product_price * quantity
                    subtotal += item_total
                    
                    # Print the product details
                    print(f"{product_name}: {quantity} @ ${product_price:.2f} = ${item_total:.2f}")
                
                except KeyError as e:
                    print("Error: Unknown product ID in request.csv")
                    print(e)
        
        # Calculate the tax and the total
        sales_tax = subtotal * sales_tax_rate
        total = subtotal + sales_tax
        
        # Print the subtotal, tax, total, and number of items
        print(f"\nNumber of items: {total_items}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax:.2f}")
        print(f"Total: ${total:.2f}")
        print("\nThank you for shopping at Inkom Emporium.")
        
        # Get the current date and time and print it
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")
    
    except FileNotFoundError as e:
        print("Error: Missing file")
        print(e)
    except PermissionError as e:
        print("Error: Permission denied while accessing the file.")
        print(e)

# Protect the call to main
if __name__ == "__main__":
    main()
