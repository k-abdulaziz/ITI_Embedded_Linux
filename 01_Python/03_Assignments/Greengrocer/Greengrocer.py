# Import the 'json' module to read and write data in JSON format.
import json

# Open the 'Products.json' file in read mode and load the contents into a dictionary.
with open('Products.json', 'r') as f:
    Products_Dict = json.load(f)

# Display a welcome message.
welcome_message = "Welcome to Khodar we Fakha!"
print(welcome_message)

# Print a line of asterisks to separate the welcome message from the rest of the output.
print("*" * len(welcome_message))
print(" ")

# Loop through the categories in the Products_Dict dictionary and print the items in each category with their prices.
for category, items in Products_Dict.items():
    print(f"{category.capitalize()}\n")
    for item, details in items.items():
        print(f"{item}: {details['price']} EGP per kg")
    print()

# Prompt the user to select items to purchase and enter the amount in kg, until the user enters 'done'.
purchase_list = []
print("\nPlease select the items you wish to purchase and enter the amount in kg. Enter 'done' when you are finished.\n")
while True:
    item = input("Item name: ")
    if item == "done":
        break
    # Check if the entered item is available, otherwise prompt the user with a message and continue the loop.
    if item not in Products_Dict["fruits"] and item not in Products_Dict["vegetables"]:
        print("Sorry, that item is not available.")
        continue
    # Prompt the user to enter the amount of the selected item in kg.
    amount = float(input("Amount in kg: "))
    # Check if the selected item is available in the required amount, otherwise prompt the user with a message and continue the loop.
    if amount > Products_Dict["fruits"].get(item, {}).get("amount", 0) + Products_Dict["vegetables"].get(item, {}).get("amount", 0):
        print("Sorry, we do not have that much amount available.")
        continue
    # Add the selected item and its amount to the purchase_list.
    purchase_list.append((item, amount))

# Display a message to thank the user for their purchase.
print("\nThank you for your purchase!\n")

# Loop through the items in the purchase_list, calculate the cost of each item, and add it to the total cost.
total_cost = 0
for item, amount in purchase_list:
    if item in Products_Dict["fruits"]:
        Products_Dict["fruits"][item]["amount"] -= amount
        price = Products_Dict["fruits"][item]["price"]
    else:
        Products_Dict["vegetables"][item]["amount"] -= amount
        price = Products_Dict["vegetables"][item]["price"]
    cost = price * amount
    total_cost += cost
    # Print the name of the item, its amount, its price per kg, and its total cost.
    print(f"{item} - {amount} kg - {price} EGP/kg - Total cost: {cost} EGP")

# Display the total cost of the purchase.
print(f"\nTotal cost: {total_cost} EGP")

# Save the updated dictionary in JSON format to the 'Products.json' file.
with open('Products.json', 'w') as f:
    json.dump(Products_Dict, f, indent=2)
