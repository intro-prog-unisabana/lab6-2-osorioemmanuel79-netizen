def show_inventory(inventory):
    print("\nCurrent Inventory:")
    # Corrección 1: usar .items() para iterar correctamente
    for fruit, stock in inventory.items():
        print(f"{fruit}: {stock}")
    print()


def add_fruit(inventory):
    fruit = input("Enter the name of the new fruit: ").strip()
    if fruit in inventory.keys():
        print(f"{fruit} already exists!\n")
    else:
        stock = input(f"Enter stock for {fruit}: ")
        # Corrección 2: usar = en vez de ==
        inventory[fruit] = int(stock)
        print(f"{fruit} added with stock {stock}.\n")


def update_stock(inventory):
    fruit = input("Enter the name of the fruit to update: ").strip()
    # Corrección 3: verificar con keys() o directamente en inventory
    if fruit in inventory:
        amount = input(f"Enter amount to add to {fruit}'s stock: ")
        # Corrección 4: convertir a int antes de sumar
        inventory[fruit] += int(amount)
        print(f"{fruit} stock increased by {amount}.\n")
    else:
        print(f"{fruit} is not in inventory. Use option 2 to add it.\n")


def menu():
    print("Options:")
    print("1 - View inventory")
    print("2 - Add new fruit")
    print("3 - Update existing fruit stock")
    print("4 - Exit")


def run_program():
    # Corrección 5: faltaban comas en el diccionario
    inventory = {
        "apples": 10,
        "bananas": 20,
        "oranges": 15
    }   