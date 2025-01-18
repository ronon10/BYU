import csv
from datetime import datetime
import os

# load inventory files
def load_inventory(file_path):
    inventory = []
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found. Please ensure the file exists with data.")
        return inventory

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            print("Headers in CSV:", reader.fieldnames)
            for row in reader:
                if any(row.values()):  # ignore blank lines
                    inventory.append({
                        'product': row['product'],
                        'price': float(row['price']),
                        'stock': int(row['stock']),
                        'sales': int(row.get('sales', 0))
                    })
            print("Inventory loaded:", inventory)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return inventory

# registry sales
def register_sale(inventory, product_name, quantity, sales_file='sales.csv'):
    for product in inventory:
        if product['product'] == product_name:
            if product['stock'] >= quantity:
                product['stock'] -= quantity
                product['sales'] += quantity
                print(f"Sale registered: {quantity} {product_name}(s) sold.")
                
                # Registrar venda
                with open(sales_file, mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # real date and time
                    writer.writerow([product_name, quantity, product['price'], timestamp])
                    print(f"Sale recorded: {product_name}, Quantity: {quantity}, Price: {product['price']}, Date: {timestamp}")
            else:
                print(f"Not enough stock for {product_name}. Available: {product['stock']}.")
            return
    print(f"Product {product_name} not found in inventory.")

# update inventory
def update_inventory(inventory, product_name, quantity):
    for product in inventory:
        if product['product'] == product_name:
            product['stock'] += quantity
            print(f"Stock updated: {product_name} now has {product['stock']} items.")
            return
    print(f"Product {product_name} not found in inventory.")

# save inventory
def save_inventory(file_path, inventory):
    if not inventory:
        print("No inventory data to save.")
        return
    
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['product', 'price', 'stock', 'sales']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for item in inventory:
                writer.writerow(item)
        print("Inventory saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving inventory: {e}")

# generate sales report
def generate_sales_report(inventory):
    report = "Sales Report:\n"
    for product in inventory:
        report += f"Product: {product['product']}, Stock remaining: {product['stock']}, Sales: {product['sales']}\n"
    return report

# check sales
def analyze_sales(inventory):
    high_performance = []
    low_performance = []
    for product in inventory:
        if product['stock'] > 10:
            low_performance.append(product['product'])
        else:
            high_performance.append(product['product'])
    return high_performance, low_performance

# predict stocking
def predict_restocking(inventory):
    to_restock = []
    for product in inventory:
        if product['stock'] < 5:
            to_restock.append(product['product'])
    return to_restock

# main function of the program
def main():
    inventory_file = 'C:/Users/realves/Documents/BYU/CSE111/week 7/products.csv'
    sales_file = 'C:/Users/realves/Documents/BYU/CSE111/week 7/sales.csv'

    # pload inventory
    inventory = load_inventory(inventory_file)

    if inventory:
        print("\n1. Registering a sale...")
        update_inventory(inventory, 'apple', 15)
        register_sale(inventory, 'apple', 3, sales_file)

        print("\n2. Updating inventory...")
        update_inventory(inventory, 'banana', 5)

        print("\n3. Generating sales report...")
        report = generate_sales_report(inventory)
        print(report)

        print("\n4. Analyzing sales performance...")
        high, low = analyze_sales(inventory)
        print(f"High performing products: {high}")
        print(f"Low performing products: {low}")

        print("\n5. Predicting restocking needs...")
        to_restock = predict_restocking(inventory)
        print(f"Products to restock: {to_restock}")

        print("\n6. Saving updated inventory...")
        save_inventory(inventory_file, inventory)
    else:
        print("No inventory loaded. Ensure the CSV file has data.")

if __name__ == "__main__":
    main()

print()
print()

# check if the product archive was found
print("File found?", os.path.exists('C:/Users/realves/Documents/BYU/CSE111/week 7/products.csv'))
print()

# view all product archive content
with open('C:/Users/realves/Documents/BYU/CSE111/week 7/products.csv', mode='r', encoding='utf-8') as file:
    print("File content:")
    for line in file:
        print(repr(line))  # show all the lines of products file
