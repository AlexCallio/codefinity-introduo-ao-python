# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")

for inventory_1 in inventory:
    print(f"Processing {inventory_1}")

    current_stock, min_stock, restock_amount, on_sale = inventory[inventory_1]
    while current_stock < min_stock:
       current_stock += restock_amount
    inventory[inventory_1][0] = current_stock
    if current_stock > discount_threshold and not on_sale:
       inventory[inventory_1][3] = True
       
print("Processing completed")
    

    