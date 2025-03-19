class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: \u20b1{self.price:.2f}"


class ItemManager:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, description, price):
        self.check_item_id(item_id)
        self.check_price(price)
        item = Item(item_id, name, description, price)
        self.items[item_id] = item
        print(f"Item added: {item}")
        return item

    def get_item(self, item_id):
        self.check_item_id(item_id)
        return self.items.get(item_id, None)

    def update_item(self, item_id, name=None, description=None, price=None):
        self.check_item_id(item_id)
        item = self.items.get(item_id)
        if not item:
            raise ValueError("Not found")

        if name:
            item.name = name
        if description:
            item.description = description
        if price is not None:
            self.check_price(price)
            item.price = price

        print(f"Item updated: {item}")
        return item

    def delete_item(self, item_id):
        self.check_item_id(item_id)
        if item_id in self.items:
            del self.items[item_id]
            print(f"ID {item_id} deleted.")
        else:
            raise ValueError("Item not found")

    def check_item_id(self, item_id):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Item ID should be positive ")

    def check_price(self, price):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price should be positive")


if __name__ == "__main__":
    manager = ItemManager()

    while True:
        print("1. Add Item")
        print("2. View Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

        option = input("Choose a number: ")

        if option == '1':
            try:
                item_id = int(input("Enter ID: "))
                name = input("Enter name: ")
                description = input("Enter description: ")
                price = float(input("Enter price: "))
                manager.add_item(item_id, name, description, price)
            except ValueError as e:
                print(f"Error: {e}")

        elif option == '2':
            try:
                item_id = int(input("Enter ID: "))
                item = manager.get_item(item_id)
                print(item if item else "Not found.")
            except ValueError as e:
                print(f"Error: {e}")

        elif option == '3':
            try:
                item_id = int(input("Enter ID: "))
                name = input("Enter new name: ")
                description = input("Enter new description: ")
                price_input = input("Enter new price: ")
                price = float(price_input) if price_input else None
                manager.update_item(item_id, name if name else None,
                                    description if description else None,
                                    price)
            except ValueError as e:
                print(f"Error: {e}")

        elif option == '4':
            try:
                item_id = int(input("Enter ID: "))
                manager.delete_item(item_id)
            except ValueError as e:
                print(f"Error: {e}")
                
        elif option == '5':
            print("Exiting")
            break

        else:
            print("Select a valid option.")
