import csv
from datetime import datetime, timedelta

# I had the "Exceeding theRequirements"
# write and print as submted
# rigth now, today, 71 days until New Year's Sale
# and print 10% off for next cup yourgurt.



def read_dictionary(filename, key_column_index):
    """
    Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    """
    dictionary = {}
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                key = row[key_column_index]
                dictionary[key] = row
    except FileNotFoundError as e:
        print("Error: Missing file")
        print(e)
        return None
    except PermissionError as e:
        print("Error: You don't have permission to read the file.")
        print(e)
        return None
    return dictionary

def calculate_discounted_price(product_id, quantity, price):
    """
    Calculate the discounted price for product D083 (buy one, get one 50% off).
    """
    if product_id == 'D083' and quantity > 1:
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return (full_price_items * price) + (half_price_items * price * 0.5)
    else:
        return quantity * price

def main():
    store_name = "Inkom Emporium"
    
    try:
        products_dict = read_dictionary('C:/Users/realves/Documents/BYU/CSE111/week 5/products.csv', 0)
        if products_dict is None:
            return

        subtotal = 0
        sales_tax_rate = 0.06
        total_items = 0
        
        with open('C:/Users/realves/Documents/BYU/CSE111/week 5/request.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)

            print(f"\n{store_name}")
            print("Purchased items:")
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])
                total_items += quantity
                
                try:
                    product_info = products_dict[product_number]
                    product_name = product_info[1]
                    product_price = float(product_info[2])

                    item_total = calculate_discounted_price(product_number, quantity, product_price)
                    subtotal += item_total

                    print(f"{product_name}: {quantity} @ ${product_price:.2f} = ${item_total:.2f}")
                
                except KeyError as e:
                    print("Error: Unknown product ID in request.csv")
                    print(e)

        sales_tax = subtotal * sales_tax_rate
        total = subtotal + sales_tax

        print(f"\nNumber of items: {total_items}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax:.2f}")
        print(f"Total: ${total:.2f}")
        print("\nThank you for shopping at Inkom Emporium.")

        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")

        # Days left for New Year's sale
        new_year = datetime(current_date_and_time.year + 1, 1, 1)
        days_until_new_year = (new_year - current_date_and_time).days
        print(f"\nReminder: {days_until_new_year} days until our New Year's Sale!")

        # Return until date (30 days from now)
        return_date = current_date_and_time + timedelta(days=30)
        print(f"Return until: {return_date:%a %b %d %Y, 21:00}")

        # Print a random coupon for one of the purchased products
        print(f"Coupon: Get 10% off your next purchase of {product_name}!")

    except FileNotFoundError as e:
        print("Error: Missing file")
        print(e)
    except PermissionError as e:
        print("Error: Permission denied while accessing the file.")
        print(e)

if __name__ == "__main__":
    main()
