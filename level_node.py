from typing import Match
import numpy as np
from enum import Enum
import random


levels = []
items = {"Potion": 25, "Med_Potion": 50, "Super_Potion": 100}
armour = {"Bronze_Helmet": 5, "Silver_Helmet": 10, "Gold_Helmet": 15, "Diamond_Helmet": 25, "Broze_Chestplate": 25,
          "Silver_Chestplate": 50, "Gold_Chestplate": 75, "Diamond_Chestplate": 100,}
weapons = {"Bronze_Sword": 25, "Silver_Sword": 50, "Gold_Sword": 100}
chest = [items, armour, weapons]
inventory = []
equip = {
    'Head': None,
    'Chest': None,
    'Legs': None,
    'Boots': None,
    'Weapon': None
}

class LevelNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.children = []

def player_tranverse(node):
    if node is None:
        print("You've reacehd a dead end!")
        return

    print(f"\nYou are at node: {node.data}")
    

    #Check if this is a leaf node
    if node.left is None and node.right is None:
        print("This is a leaf node. No further moves.")
        return 

    choices = []
    if node.left:
        print("L: Go to left child", node.left.data)
        choices.append('L')
    if node.right:
        print("R: Go to right child", node.right.data)
        choices.append('R')

    while True:
        choice = input("Choose your next move (" + "/".join(choices) + "): ").strip().upper()
        if choice == 'L' and 'L' in choices:
            player_tranverse(node.left)
            break
        elif choice == 'R' and 'R' in choices:
            player_tranverse(node.right)
            break
        else:
           print("Invalid choice. Try again")

class GameMenu():
  def __init__(self):
    self.option = None
    self.menu = None
    self.quit_game = False
    self.create_menu() # Call create_menu here

  def create_menu(self):
    self.menu = {"Start Game:": self.start_game, "Quit Game": self.quit_game}
    UP = "W"
    DOWN = "S"
    LEFT = "A"
    RIGHT = "D"

  def start_game(self): # Define a placeholder start_game method
      print("Starting the game...")


class Rooms():
  def __init__(self):
    self.direction = ["Right room", "Left room", "Front room", "Go Back"]

  def randum_room(self):
    rand_room = []
    available_directions = self.direction[:] # Create a copy of the direction list
    randum_gen = np.random.randint(1, len(available_directions) + 1) # Ensure randum_gen is within bounds
    while len(rand_room) < randum_gen and available_directions: # Add check for available_directions
      chosen_direction = np.random.choice(available_directions)
      rand_room.append(chosen_direction)
      available_directions.remove(chosen_direction) # Remove chosen direction from the copy
    return rand_room



class Monsters():
  def __init__(self,name,health,strength):
    self.name = name
    self.health = health
    self.strength = strength

  def attack(self, other):
    other.health -= self.strength
    print(f"{self.name} attacks {other.name} for {self.strength} damage. ")
    print(f"{other.name} has {other.health} health remaining.")
    if other.health <= 0:
      print(f"{other.name} has been defeated!")
      return True
    else:
      return False

class Hero():
  def __init__(self,name,health,strength,protection):
    super().__init__()
    self.name = name
    self.health = health
    self.strength = strength
    self.protection = protection

  def __str__(self):
    return f"{self.name} is {self.age} years old and has {self.health} health and {self.strength} strength."

  def attack(self, other):
    other.health -= self.strength
    print(f"{self.name} attacks {other.name} for {self.strength} damage. ")
    print(f"{other.name} has {other.health} health remaining.")
    if other.health <= 0:
      print(f"{other.name} has been defeated!")
      return True
    else:
      return False

  def restore(self,other,potion):
    self.health += items.get(potion)
    print(f"{self.name} has restored {items.get(potion)} health.")
    print(f"{self.name} has {self.health} health remaining.")

villager = Hero("Bob", 100, 5, 0)
troll = Monsters("Troll", 100, 20)
goblin = Monsters("goblin", 60,15)

monster = [troll, goblin]

ran_mon = np.random.choice(monster)



Menu = GameMenu()
room_gen = Rooms() # Create an instance of the Rooms class


def main():
    root = LevelNode(0)
    node1 = LevelNode(1)
    node2 = LevelNode(2)
    node3 = LevelNode(3)
    node4 = LevelNode(4)
    node5 = LevelNode(5)
    node6 = LevelNode(6)
    node7 = LevelNode(7)
    node8 = LevelNode(8)

    root.left = node1
    root.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5
    node2.right = node6

    node3.left = node7
    node3.right = node8

    print("Starting interactive transversal")
    player_tranverse(root)
    
    while Menu.quit_game == False:
      print("Welcome to the game!")
      print("Please select an option:")
      print("1. Start Game")
      print("2. Quit Game")

      choice = input("Enter your choice: ")

      match choice:
        case "1":
          Menu.start_game()

          # Generate 10 levels with random rooms
          levels = [room_gen.randum_room() for _ in range(10)]
          current_level_index = 0

          while current_level_index < len(levels) and not Menu.quit_game:
            current_room = levels[current_level_index]
            print(f"\nLevel {current_level_index + 1}: {current_room}\n")
            print("You enter the room")
            print(f"\nWhich room will you to enter? {current_room}\n")

            # Present available directions to the user
            for i, direction in enumerate(current_room):
                print(f"{i + 1}. {direction}")

            choice = int(input("Enter your choice:")) # Convert input to integer here

            if 1 <= choice <= len(current_room):
                selected_direction = current_room[choice - 1]
                print(f"You enter the {selected_direction}\n")

                if selected_direction == "Go Back":
                    if current_level_index > 0:
                        current_level_index -= 1
                        print("You went back to the previous level.")
                    else:
                        print("You are already at the first level, you cannot go back further.")
                        # Add a continue statement here to go back to the start of the inner while loop
                        continue
                else:
                    # Randomly determine what's in the room
                    room_event = random.choice(["chest", "monster", "empty"])

                    if room_event == "chest":
                        random_item_category = np.random.choice(chest)
                        random_item = np.random.choice(list(random_item_category))

                        open_chest = input(f"\nYou found a chest!\n Would you like to open it?: \n")
                        if open_chest.lower() == 'y':
                          random_item_category = np.random.choice(chest)
                          random_item = np.random.choice(list(random_item_category))

                          if random_item in items:
                            add_to_inventory = input(f"\nYou Pulled a {random_item} from the chest! \nWould you like to add it to your Inventory? (y/n): \n")
                            if add_to_inventory.lower() == 'y':
                              inventory.append(random_item)
                              print(f"Your current inventory: {inventory}")
                            else:
                              print("\nYou did not add the item to your inventory.\n")
                          elif random_item in armour or random_item in weapons: # Check if it's armor or a weapon
                             equip_item = input(f"You Pulled a {random_item} from the chest! \n Would you like to Equip it? (y/n): \n")
                             if equip_item.lower() == 'y':
                                if random_item in armour:
                                    if "Helmet" in random_item:
                                       equip['Head'] = random_item
                                       villager.protection += armour[random_item]

                                    elif "Chestplate" in random_item:
                                       equip['Chest'] = random_item
                                       villager.protection += armour[random_item]

                                    elif "Leg" in random_item:
                                       equip['Legs'] = random_item
                                       villager.protection += armour[random_item]

                                elif random_item in weapons:
                                   equip['Weapon'] = random_item
                                   villager.strength += weapons[random_item]

                                print(f"Your current Equipment: {equip}")
                             else:
                                print("You did not equip the item.")

                          else:
                            print("You found something unidentifiable.")

                        else:
                          print("You did not open the chest.")

                    elif room_event == "monster":
                      ran_mon = np.random.choice(monster)
                      print(f"\nYou encountered a {ran_mon.name}!\n")
                      defeat = False
                      while defeat == False:

                        # Implement monster encounter/combat logic here
                        action = int(input("1.Attack\n2.Defend\n3.Run\n4.Inventory\n"))

                        match action:
                          case 1:
                            print("\nYou attacked the monster\n")
                            villager.attack(ran_mon)
                            print(f"monster health: {ran_mon.health}")
                            if ran_mon.health <= 0:
                              defeat = True
                              ran_mon.health = 60

                          case 2:
                            print("\nYou defended the monster\n")
                            villager.health += 10
                          case 3:
                            print("\nYou ran away from the monster\n")
                            defeat = True
                            break
                          case 4:
                            print(f"Your current inventory: {inventory}")
                            pick = int(input("Pick Potion \n 1.potion\n2.Med potion\n3.Super potion\n"))

                            match pick:
                              case 1:
                                villager.restore(villager,"Potion")
                                print(f"Your current inventory: {inventory}")
                              case 2:
                                villager.restore(villager,"Med_Potion")
                                print(f"Your current inventory: {inventory}")
                              case 3:
                                villager.restore(villager,"Super_Potion")

                            print(f"\nYour health {villager.health}\n")

                          case _:
                            print("Invalid Input")

                        if not defeat: # Only monster attacks if not defeated

                          reduction = (villager.protection * .20)
                          ran_mon.strength -= reduction

                          print(f"\nmonster attacks\n")
                          ran_mon.attack(villager)

                          print(f"villager health: {villager.health}\n")
                          if villager.health <= 0:
                            defeat = True


                    else: # empty room
                        print("\nYou entered an empty room.")

                    # Move to the next level if not going back
                    if selected_direction != "Go Back":
                        current_level_index += 1
            else:
                print("Invalid Input")


        case "2":
          Menu.quit_game = True
        case _:
          print("Invalid choice. Please try again.")

    print("Thank you for using the game!")


if __name__ == "__main__":
    main()
