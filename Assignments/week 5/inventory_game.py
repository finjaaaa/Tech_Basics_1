# --- Game State ---
inventory = []
items_in_room = [
    {"name": "Torch", "type": "tool", "description": "Lights up dark places."},
    {"name": "Apple", "type": "food", "description": "Restores a small amount of health."},
    {"name": "Key", "type": "tool", "description": "Opens a locked door."}
] # length shall be larger than max inventory size if there is only one room
MAX_INVENTORY_SIZE = 5

# --- Functions ---

def show_inventory():
    if not inventory:
        print("No items to show.")
    else:
        print("Inventory includes:")
        for item in inventory:
            print("-" + item["name"] + "(" + str(item["type"]) + ")")


def show_room_items():
   if not items_in_room:
       print("The room is empty")
   else:
       print("In the room, you'll find:")
       for item in items_in_room:
           print("-" + item["name"] + ":" + item.get("description", ''))


def pick_up(item_name):
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your inventory is full.")
        return
    for item in items_in_room:
        if item["name"].lower() == item_name.lower():
            inventory.append(item)
            items_in_room.remove(item)
            print(item["name"] + "item picked up.")
            return
    print(item["name"] + "isn't in the room.")


def drop(item_name):
   for item in inventory:
       if item["name"].lower() == item_name.lower():
           inventory.remove(item)
           print(item["name"] + "item dropped.")
           return
   print(item_name + "isn't in your inventory.")


def use(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            if item["type"] == "food":
                print("You're eating" + item["name"])
                inventory.remove(item)
            elif item["type"] == "tool":
                if item["name"].lower() == "key":
                    print("You're using the key to unlock the door. Congratulations! You've won the game.")
                    global game_running
                    game_running = False
                    return
                else:
                    print("You're using" + item["name"])
            else:
                print(item["name"] + "can't be used.")
            return
    print(item_name + "isn't in your inventory.")

def examine(item_name):
    for item in inventory + items_in_room:
        if item['name'].lower() == item_name.lower():
            print(item['name'] + ":" + item.get('description', 'no description.'))
            return
    print(item_name + "isn't in your room or inventory.")


# --- Game Loop ---
game_running = True

def game_loop():
    print("Welcome to the Inventory Game!")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            # You can also rename the commands according to your own needs
            print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], quit")
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            item_name = command[7:]
            pick_up(item_name)
        elif command.startswith("drop "):
            item_name = command[5:]
            drop(item_name)
        elif command.startswith("use "):
            item_name = command[4:]
            use(item_name)
        elif command.startswith("examine "):
            item_name = command[8:]
            examine(item_name)
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()
