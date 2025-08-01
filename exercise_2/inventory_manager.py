inventory = {}

def add_new_item(name, price, stock, category):
    if name and price > 0 and stock >= 0 and category:
        inventory[name] = {
            "price": price,
            "stock": stock,
            "category": category
        }
        return f"Successfully added item to inventory\nInventory:\n{inventory}\n"
    else:
        return "Please make sure that all values are present and price > 0 and stock >= 0\n"
    

def update_stock(name, value):
    if name and name in inventory:
        inventory[name]["stock"] += value
        stock = inventory[name]["stock"]
        if stock == 0:
            print(f"Deleting {name} from inventory because stock is zero")
            del inventory[name]
        return f"Stock updated\nInventory:\n{inventory}\n"
    return "Stock update failed\n"
    


def search_by_category(category):
    result = []
    for key, value in inventory.items():
        if value["category"] == category:
            result.append(key)

    res = f"Found {len(result)} items in {category}\n"
    for item in result:
        res += f"* {item} - ${inventory[item]["price"]:.2f} ({inventory[item]["stock"]} units remaining)\n"
    return res


def check_low_stock():
    low_stock_items = []
    for key, value in inventory.items():
        if value["stock"] <= 5:
            low_stock_items.append(key)

    res = "LOW STOCK ALERT\n\n"
    for item in low_stock_items:
        res += f"- {item} ({inventory[item]["stock"]}) units remaining"
    return res


def total_inventory_value():
    inventory_value = 0
    for value in list(inventory.values()):
        inventory_value += value["price"] * value["stock"]
    
    return f"Total inventory value: ${inventory_value:.2f}"


def entry():
    print("\n******** WELCOME! LET'S MANAGE YOUR INVENTORY *********\n")
    while True:
        choice = input("1. Add new item\n2. Update stock\n3. Search by category\n4. Check low stock\n5. Check total inventory value\n6. Exit\n\nChoice:  ")
        if choice == "1":
            try:
                name = input("Enter item name: ")
                price = float(input("Enter item price: "))
                stock = int(input("Enter amount of item available: "))
                category = input("Category for item: ")
            except ValueError:
                print("Please enter the appropriate inputs as prompted")

            print(add_new_item(name, price, stock, category))
            
        elif choice == "2":
            try:
                name = input("Enter item name to update stock: ")
                stock = int(input("Enter stock update value\n(positive for increment, negative for decrement):  "))
            except ValueError:
                print("Please enter the appropriate types as prompted")

            print(update_stock(name, stock))
        
        elif choice == "3":
            category = input("Enter category: ")
            print(search_by_category(category))

        elif choice == "4":
            print(check_low_stock())
        
        elif choice == "5":
            print(total_inventory_value())
        
        elif choice == "6":
            print("Cleaning up system..........")
            break
        else:
            print("\nPlease eneter a number corresponding to an item on the list\n")



entry()




