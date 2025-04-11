customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
price = int(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
subtotal = price * quantity
tax_rate = 0.08
tax = subtotal * tax_rate
total = subtotal + tax
print("INVOICE")
print(f"Customer: {customer_name}")
print(f"Product: {product_name}")
print(f"Price : ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total : ${total:.2f}")
