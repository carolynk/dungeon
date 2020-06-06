
import colors
from rooms import Person, Map, Item, Inventory

inventory = []

def create_dungeon():
    dungeon = Map()
    
    # Create Rooms
    dungeon.add_room("The Hole", "You have fallen down a hole into a dungeon.")
    dungeon.add_room("The Cave", "A dark cave. You can't see anything.")
    dungeon.add_room("The Falls", "An underground waterfall to the east rushes from the ceiling.")
    dungeon.add_room("The Bunker",
                  "A long room with dozens of bunkbeds line the walls. They look long abandoned. Cobwebs are everywhere.")
    dungeon.add_room("The Control Center",
                   "There are three giant panels here with blinking lights and hundreds of knobs and buttons. There is what looks like a pilot seat facing a wide screen.")
    dungeon.add_room("The Inhouse",
                   "There are hundreds of toilets here, some even with the carcus of fish, urine, and feces. Eww!!!") 
    dungeon.add_room("The Treasure Palace",
                   "'Am I rich?' you ask yourself as you see a room full of treasure, including gold, silver, diamonds!")

    #Aboveground  
    dungeon.add_room("The Farm",
                "Stairs lead to a light doorway. You the realize it is aboveground! Then cows, sheep, and some chicken signal it is a farm. You shouldn't stay here long.")  
    dungeon.add_room("The Lake-Mere",
                   "A poluted waterfall runs down a smokestack. You shouldn't stay here long.")
    dungeon.add_room("The Forest",
                   "High oak trees surround you on all sides in all directions. There is a pile of leaves here.")
    dungeon.add_room("The Roadside",
                "There is an old dirt road here with a shiny lime Lamborghini. Your best friend is standing next to it.")                 

    # Add doors
    dungeon.add_door("The Hole", "The Cave", "e")
    dungeon.add_door("The Cave", "The Farm", "u")

    # Add hiddendoor
    dungeon.add_hidden_door("The Falls", "The Treasure Palace", "e")

    # Control center doors
    dungeon.add_door("The Control Center", "The Cave", "w")
    dungeon.add_door("The Control Center", "The Falls", "n")
    dungeon.add_door("The Control Center", "The Bunker", "s")
    dungeon.add_door("The Control Center", "The Inhouse", "e")

    # Create inventory
    # inventory = Inventory()

    # Add Items
    hole = dungeon.get_room("The Hole")
    rope = Item("Rope", "A long, sturdy rope")
    hole.items.append(rope)

    farm = dungeon.get_room("The Farm")
    meat = Item("Meat", "A chunk of thick juicy meat")
    farm.items.append(meat)

    inhouse = dungeon.get_room("The Inhouse")
    plunger = Item("Plunger", "A long skinny stick, with a rubber suction thing at the end")
    inhouse.items.append(plunger)

    control_center = dungeon.get_room("The Control Center")
    diagram = Item("diagram", "A map of the place")
    control_center.items.append(diagram)

    bunker = dungeon.get_room("The Bunker")
    key = Item("key", "A " + colors.cyan + "cyan" + colors.blue + "key, looks like it would go in a fancy door lock")
    bunker.items.append(key)

    cave = dungeon.get_room("The Cave")
    alarm_clock = Item("clock", "A old fashioned lime green alarm clock.")
    cave.items.append(alarm_clock)

    return dungeon


def find_doors(room):
    """
    Parameters
    ----------
    room: Room
      where the player currently is
    """
    direction = ""
    if 'e' in room.doors:
        direction = "east"
    if 'w' in room.doors:
      if direction:
        direction = direction + ", "
      direction = direction + "west"
    if 'n' in room.doors:
      if direction:
        direction = direction + ", "
      direction = direction + "north"
    if 's' in room.doors:
      if direction:
        direction = direction + ", "
      direction = direction + "south"
    if 'u' in room.doors:
        if direction:
          direction = direction + ", "
        direction = direction + "upward"
    if 'd' in room.doors:
        if direction:
          direction = direction + ", "
        direction = "downward"    

    if not room.doors:
        print("You are trapped, there are no doors")
    else:
        print(colors.orange + "There is a door leading " + direction)

def above_ground(dungeon, turns):
    if turns <= 3:
      dungeon.add_trap_door("The Lake-Mere", "The Cave", "d")
      if turns == 3:
          print("The opening below is slowly closing.")
    elif 3 < turns <= 6:
      dungeon.add_trap_door("The Farm", "The Cave", "d")
      if turns == 6:
          print("The opening below is slowly closing.")
    elif 6 < turns <= 9:
      dungeon.add_trap_door("Roadside", "The Cave", "d")
      if turns == 9:
          print("The opening below is slowly closing.")
    else:
      dungeon.add_trap_door("The Forest", "The Cave", "d")
      if turns == 12:
          print("The opening below is slowly closing.")
    

      

def get_menu():
    return """
n - go north
s - go south
e - go east
w - go west
l - look more closely
t - take all
i - inventory
u - up
d - down
"""


def play():
    ans = ''
    dungeon = create_dungeon()
    print(colors.green + """Welcome to the Underground.""" 
    + colors.pink + "\n(You can type " + colors.default + "help" 
    + colors.pink + " anytime to see options.)\n")
    current_room = dungeon.rooms["The Hole"]
    print(colors.green + current_room.name)
    print(colors.pink + current_room.description)

    if current_room.people:
        print(str(current_room.people[0].name) + " is here.")
    turns = 1
    while ans != 'q':
        if turns <= 3:
          dungeon.add_trap_door("The Cave", "The Lake-Mere",  "u")
        elif 3 < turns <= 6:
          dungeon.add_trap_door("The Cave", "The Farm", "u")
        elif 6 < turns <= 9:
          dungeon.add_trap_door("The Cave", "Roadside", "u")
        else:
          dungeon.add_trap_door("The Cave", "The Forest", "u")

        find_doors(current_room)
        ans = input(colors.default + """> """)
        reply = ""
        if ans == "help":
            reply = get_menu()
        elif ans == "e" or ans == "w" or ans == "n" or ans == "s" or ans == "u" or ans == "d":
            if dungeon.walk(current_room, ans) is not None:
                current_room = dungeon.walk(current_room, ans)
        elif ans == "ask" and current_room.people:
            current_room.people[0].ask()
        elif ans == "l" or ans == "look":
            reply = colors.blue + "You look more closely and see"
            if not current_room.items:
                reply = reply + " nothing"
            for item in current_room.items:
                reply = reply + "\n" + str(item.name)
        elif ans == "take" or ans == "t":
            if current_room.items:
                reply = colors.blue + "You take the items in the room:"
            else:
                reply = "There are no items in the room to take."
            for item in current_room.items:
                reply = reply + "\n" + str(item.name)
                current_room.items.pop()
                inventory.append(item)
        elif ans == "i":
            reply = "Your bag contains:"
            for item in inventory:
                reply = reply + " " + item.name
        elif ans == "q":
            exit()
        else:
            reply = "I don't understand. You can type help to see options."
        if turns < 12:
          turns = turns + 1
        else:
          turns = 1
        
        # Print room and new info
        print("")
        print(colors.green + current_room.name + "\n" + colors.pink + current_room.description)
        if reply:
          print(reply)
        for item in inventory:
          if item.name == "clock":
            print(colors.cyan + "The alarm clock reads: " + str(turns) + ":00 O'Clock")
        outside = ["The Roadside", "The Lake-Mere", "The Forest", "The Farm"]
        
        if current_room.name in outside:
          above_ground(dungeon, turns)

        if current_room.people:
            print(str(current_room.people[0].name) + " is here.")


        if current_room.name == "Roadside":
          print("There you are!' they say. 'I've been looking for you for " + str(turns + 1) + " Hours!!! 'Let's get out of here, this place is giving me the creeps.' \n You escaped. \n \n " + colors.green + "THE END.")                            
play()
