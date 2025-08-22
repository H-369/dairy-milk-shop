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

order = {}
while True:
    choice = input("\nWhat would you like to buy? (Type 'done' to finish): ").capitalize()

    if choice == "Done":
        break

    if choice in items:
        unit = items[choice]["unit"]
        price = items[choice]["price"]

        if unit in ["kg", "liter"]:
            qty = float(input(f"How many {unit} of {choice} do you want? "))
        else:
            qty = int(input(f"How many {unit}s of {choice} do you want? "))

        order[choice] = order.get(choice, 0) + qty
    else:
        print("❌ Sorry, item not available!")

print("\n===== Your Bill =====")
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


# ------------------ VEGETABLE SHOP ------------------_
#Second code:
#It’s about a Grocery Store:
#________________________________________________________________________
#Bismillah Mart (Vegetable Shop)

print("🥕 Welcome to Bismillah Vegetable Shop 🥔\n")

vegetables = {
    "Potato": 60,
    "Onion": 80,
    "Tomato": 100,
    "Carrot": 90,
    "Cabbage": 70,
    "Cauliflower": 120,
    "Spinach": 50,
    "Peas": 150,
    "Cucumber": 60,
    "Brinjal": 80,
    "Capsicum": 130
}

print("----- Available Vegetables (per Kg) -----")
for veg, price in vegetables.items():
    print(f"{veg} : Rs {price} per Kg")


order = {}
total = 0

while True:
    choice = input("\n👨‍🌾 Shopkeeper: What vegetable do you want? (or type 'done' to finish): ").title()
    
    if choice == "Done":
        break
    elif choice in vegetables:
        unit = input("Do you want in 'kg' or 'g'? ").lower()
        try:
            qty = float(input(f"How much {choice} do you want (in {unit})? "))
            
            if qty <= 0:
                print("❌ Please enter a valid quantity.")
                continue
            
            # Convert grams to Kg if needed
            if unit == "g":
                qty = qty / 1000  # convert grams to kilograms
            
            cost = vegetables[choice] * qty
            total += cost
            order[choice] = order.get(choice, 0) + qty
            print(f"✅ Added {qty:.2f} Kg {choice}. Current Bill: Rs {total:.2f}")
        except ValueError:
            print("❌ Please enter a number for quantity.")
    else:
        print("❌ Sorry, we don't have that vegetable.")

print("\n🧾 ----- BILL RECEIPT -----")
print("        Bismillah Shop        ")
print("-------------------------------")

for veg, qty in order.items():
    price = vegetables[veg]
    cost = price * qty
    print(f"{veg} ({qty:.2f} Kg) : Rs {cost:.2f}")

print("-------------------------------")
print(f"TOTAL BILL : Rs {total:.2f}")
print("🙏 Thank you for shopping at Bismillah Shop! 🙏")