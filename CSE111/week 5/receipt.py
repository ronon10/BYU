import csv

# read_dictionary as a function
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
    with open(filename, 'rt') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header 👌
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    
    return dictionary

# Main function 💸💸💸💸
# 6.0
def main():
    # Read the products.csv file
    # 6.1
    products_dict = read_dictionary('C:/Users/realves/Documents/BYU/CSE111/week 5/products.csv', 0)
    
    # 6.2
    print("Products Dictionary:", products_dict)
    
    # initialize variables for calculating the subtotal
    subtotal = 0
    sales_tax_rate = 0.06  # tax 6%
    
    # open and read the request.csv file
    with open('C:/Users/realves/Documents/BYU/CSE111/week 5/request.csv', 'r') as file: #6.3
        reader = csv.reader(file)
        next(reader)  # Skip the header 6.4
        
        print("\nPurchased items:")

        # 5.0
        for row in reader:
            product_number = row[0]
            quantity = int(row[1])
            
            # look up the product in the dictionary
            if product_number in products_dict:
                product_info = products_dict[product_number]
                product_name = product_info[1]
                product_price = float(product_info[2])
                
                # calculate the subtotal for this item
                item_total = product_price * quantity
                subtotal += item_total
                
                # print the product details
                print(f"{product_name}: {quantity} @ ${product_price:.2f} = ${item_total:.2f}")
    
    # calculate the tax and the total
    sales_tax = subtotal * sales_tax_rate
    total = subtotal + sales_tax
    
    # print the subtotal, tax, and total
    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}")

# Protect the call to main
if __name__ == "__main__":
    main()
