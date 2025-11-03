# Simple Purchase Calculator

# 1. Ask the user for the item name
item_name = input("Enter the item name: ")

# 2. Ask for the price of a single item
price = float(input("Enter the item price: "))

# 3. Ask for the quantity
quantity = int(input("Enter the quantity: "))

# 4. Calculate the subtotal
subtotal = price * quantity

# 5. Calculate the sales tax (7.75%)
sales_tax = subtotal * 0.0775

# 6. Calculate the total
total = subtotal + sales_tax

# 7. Display the receipt
print("\n--- RECEIPT ---")
print(f"Item: {item_name}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")
