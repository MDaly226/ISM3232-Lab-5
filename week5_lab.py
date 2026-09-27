# week5_lab.py
# Author: Michael Daly
# Businedd domain: insert name

product_name = "Laptop"  # String
status = "Pending"  # String
quantity = 5  # Integer
unit_price = 159.99  # Float
is_over_limit = unit_price * quantity > 2500  # Boolean

print(
    type(product_name),
    type(status),
    type(unit_price),
    type(quantity),
    type(is_over_limit),
)

subtotal = unit_price * quantity
tax = subtotal * 0.07
total = subtotal + tax
requires_approval = total > 1000

print("=== Purchase Request Summary ===")
print(f"Product: {product_name}")
print(f"Qty: {quantity}")
print(f"Subtotal: ${subtotal:,.2f}")
print(f"Tax: ${tax:,.2f}")
print(f"Total: ${total:,.2f}")
print(f"Requires approval: {requires_approval}")

# Step 6
user_qty = int(input("Enter a new quantity: "))  # convterts a str into an int
new_total = unit_price * user_qty * 1.07
print(f"New total for {user_qty} units: ${new_total:,.2f}")
print(f"Requires approval: {new_total > 1000}")

# step 7
