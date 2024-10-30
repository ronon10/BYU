import csv


def main():







# this part of program read the csv file and return to file
def load_inventory(file_path):
    inventory = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                inventory.append({
                    'product': row['product'],
                    'price': float(row['price']),
                    'stock': int(row['stock'])
                })
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return inventory


# this function is to register the sale and register the quatity of stoque
def register_sale(inventory, product_name, quantity):
    for product in inventory:
        if product['product'] == product_name:
            if product['stock'] >= quantity:
                product['stock'] -= quantity
                print(f"Sale registered: {quantity} {product_name}(s) sold.")
            else:
                print(f"Not enough stock for {product_name}. Available: {product['stock']}.")
            return
    print(f"Product {product_name} not found in inventory.")


# this function is for update the inventory
def update_inventory(inventory, product_name, quantity):
    for product in inventory:
        if product['product'] == product_name:
            product['stock'] += quantity
            print(f"Stock updated: {product_name} now has {product['stock']} items.")
            return
    print(f"Product {product_name} not found in inventory.")


# this function is for sales report
def generate_sales_report(inventory):
    report = "Sales Report:\n"
    for product in inventory:
        report += f"Product: {product['product']}, Stock remaining: {product['stock']}\n"
    return report



#this function is to sales analyze
def analyze_sales(inventory):
    high_performance = []
    low_performance = []
    for product in inventory:
        if product['stock'] > 10:  # Supondo que produtos com estoque alto são de baixa performance
            low_performance.append(product['product'])
        else:
            high_performance.append(product['product'])
    return high_performance, low_performance


# this funtion is to restocking
def predict_restocking(inventory):
    to_restock = []
    for product in inventory:
        if product['stock'] < 5:  # Threshold de reabastecimento
            to_restock.append(product['product'])
    return to_restock





if __name__ == "__main__":
    main()
