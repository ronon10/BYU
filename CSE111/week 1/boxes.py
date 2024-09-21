#first I import the math's module
import math

# created the variables
items_manuf = int(input(f"Enter the number of items: "))
items_per_box = int(input(f"Enter the number of items per box: "))

# making the division math 
num_boxes = math.ceil(items_manuf / items_per_box)

print()
print(f"For {items_manuf} items, packing {items_per_box} items in each box, you will need {num_boxes} boxes.")
