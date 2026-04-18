# קבועים
BASE_PRICE = 12.0

# תוספות זולות
cheap_toppings = {
    "olives": 2.0,
    "mushrooms": 2.0,
    "corn": 2.0,
    "onion": 2.0
}

# תוספות יקרות
expensive_toppings = {
    "bulgarian_cheese": 3.0,
    "extra_cheese": 3.0,
    "tuna": 3.0
}

# הצגת האפשרויות למשתמש
print("Available cheap toppings:", ", ".join(cheap_toppings.keys()))
print("Available expensive toppings:", ", ".join(expensive_toppings.keys()))

# קלט מהמשתמש
cheap_input = input("Enter cheap toppings separated by commas (or press Enter for none): ")
expensive_input = input("Enter expensive toppings separated by commas (or press Enter for none): ")

# עיבוד הקלט — הפיכה לרשימה של תוספות
cheap_selected = [t.strip() for t in cheap_input.split(",") if t.strip() != ""]
expensive_selected = [t.strip() for t in expensive_input.split(",") if t.strip() != ""]

# חישוב המחיר הכולל
total = BASE_PRICE

for topping in cheap_selected:
    if topping in cheap_toppings:
        total += cheap_toppings[topping]
    else:
        print(f"Warning: '{topping}' not found in cheap toppings list.")

for topping in expensive_selected:
    if topping in expensive_toppings:
        total += expensive_toppings[topping]
    else:
        print(f"Warning: '{topping}' not found in expensive toppings list.")

# פלט סופי
print(f"Please pay {float(total)} ILS")

