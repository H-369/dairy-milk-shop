#__________________________________________________________
# MID_EXAM_PROJECT.py
# Group member names:
# 1) HANIFULLAH , 2) ARQAM SALEEM , 3) NAIMAT ALI
#___________________________________________________________

# First code:
# it's about a DAIRY MILK SHOP: 
print("===== Welcome to Bismillah Dairy Milk Shop =====")

items = {
    "Milk": {"price": 120, "unit": "liter"},
    "Curd": {"price": 150, "unit": "kg"},
    "Lassi": {"price": 100, "unit": "liter"},
    "Bread": {"price": 70, "unit": "piece"},
    "Egg": {"price": 20, "unit": "piece"},
    "Ghee": {"price": 1000, "unit": "kg"}   # clarified butter
}

# Display items
print("\nAvailable Items:")
for i, (item, details) in enumerate(items.items(), start=1):
    print(f"{i}. {item} - Rs.{details['price']} per {details['unit']}")

order = {} #to store the item which is buy by the costumers 
while True:
    choice = input("\nWhat would you like to buy? (Type 'done' to finish): ").capitalize()

    if choice == "Done":
        break

    if choice in items:
        unit = items[choice]["unit"]
        price = items[choice]["price"]

        if unit in ["kg", "liter"]:
            qty = float(input(f"How many {unit} of {choice} do you want? ")) # for decimal value 
        else:
            qty = int(input(f"How many {unit}s of {choice} do you want? ")) # for whole number value

        order[choice] = order.get(choice, 0) + qty
    else:
        print("❌ Sorry, item not available!") #print if the item is not available 

print("\n===== Your Bill =====") # to print bill reciept
total = 0
for item, qty in order.items():
    unit = items[item]["unit"]
    price = items[item]["price"]
    cost = price * qty
    print(f"{item} ({qty} {unit}) = Rs.{cost}")
    total += cost

print("--------------------------")
print(f"Total Bill: Rs.{total}")
print("===== Thank you for shopping at Bismillah Dairy Milk Shop! =====")

