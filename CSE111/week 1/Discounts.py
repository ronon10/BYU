
import math
from datetime import datetime


disc_rate = 0.10
tax_rate = 0.06

subtotal = float(input("Please, enter the subtotal: $"))

# obtando a hora
today_day = datetime.now()

# Obtendo o dia da semana (0 = segunda, 1 = terça, ... 6 = domingo)
week_day = today_day.weekday()

# If the subtotal is greater than 50 and today is
# Tuesday or Wednesday, compute the discount amount
if subtotal >= 50 and (week_day == 1 or week_day == 2):
    discount = round(subtotal * disc_rate, 2)
    print(f"Discount amount: {discount:.2f}")
    subtotal -= discount

# Compute the sales tax. Notice that we compute the sales tax
# after computing the discount because the customer does not
# pay sales tax on the full price but on the discounted price.
sales_tax = round(subtotal * tax_rate, 2)
print(f"sales tax amount: {sales_tax:.2f}")

total = subtotal + sales_tax

print(f"Total = {total:.2f}")




