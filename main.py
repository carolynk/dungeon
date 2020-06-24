import colors
from rooms import Map, Player

# from rooms import NPC
inventory = []


def create_dungeon():
    player = Player()
    dungeon = Map()

    # Create Rooms
    dungeon.add_room("The Hole", "You have fallen down a hole into a dungeon.")
    dungeon.add_room("The Cave", "A dark cave. You can't see anything.")
    dungeon.add_room("The Falls", "An underground waterfall to the east rushes from the ceiling.")
    dungeon.add_room("The Bunker",
                     "A long room with dozens of bunkers line the walls. They look long abandoned. Cobwebs are "
                     "everywhere.")
    dungeon.add_room("The Control Center",
                     "There are three giant panels here with blinking lights and hundreds of knobs and buttons. There "
                     "is what looks like a pilot seat facing a wide screen.")
    dungeon.add_room("The Inhouse",
                     "There are hundreds of toilets here, some even with the carcus of fish, urine, and feces. Eww!!!")
    dungeon.add_room("The Treasure Palace",
                     "'Am I rich?' you ask yourself as you see a room full of treasure, including gold, silver, "
                     "diamonds!")
    dungeon.add_room("Hunger",
                     "A lion is now blocking the exit, and you hear a large stomach growl")

    # Above ground
    dungeon.add_room("The Farm",
                     "Stairs lead to a light doorway. You the realize it is above ground! Then cows, sheep, and some "
                     "chicken signal it is a farm. You shouldn't stay here long.")
    dungeon.add_room("The Lake-Mere",
                     "A polluted waterfall runs down a smokestack. You shouldn't stay here long.")
    dungeon.add_room("The Forest",
                     "High oak trees surround you on all sides in all directions. There is a pile of leaves here.")
    dungeon.add_room("The Roadside",
                     "There is an old dirt road here with a shiny lime Lamborghini. Your best friend is standing next "
                     "to it.")

    # Add doors
    dungeon.add_door("The Hole", "The Cave", "e")
    dungeon.add_trap_door("The Treasure Palace", "Hunger", "u", locked=True, unlock="Rope")
    dungeon.add_trap_door("Hunger", "The Treasure Palace", "d", locked=True, unlock="Meat")
    # Add hidden doors
    dungeon.add_door("The Falls", "The Treasure Palace", "e", locked=True, unlock="key", hidden=True)

    # Control center doors
    dungeon.add_door("The Control Center", "The Cave", "w")
    dungeon.add_door("The Control Center", "The Falls", "n")
    dungeon.add_door("The Control Center", "The Bunker", "s")
    dungeon.add_door("The Control Center", "The Inhouse", "e")

    # Create inventory

    # Add Items
    hole = dungeon.get_room("The Hole")
    hole.add_item("Rope", "A long, sturdy rope")
    hole.add_gold(1)

    cave = dungeon.get_room("The Cave")
    cave.add_item("clock", "A old fashioned " + colors.green + "lime green " + colors.cyan + "alarm clock.")

    farm = dungeon.get_room("The Farm")
    farm.add_item("Meat", "A chunk of thick juicy meat")

    inhouse = dungeon.get_room("The Inhouse")
    inhouse.add_item("Mop", "A large mop.")

    hunger = dungeon.get_room("Hunger")
    hunger.add_item("Bucket", "A large metal bucket with a handle over the top.")

    control_center = dungeon.get_room("The Control Center")
    control_center.add_item("Map", "A map of the place")

    bunker = dungeon.get_room("The Bunker")
    bunker.add_item("key", "A " + colors.cyan + "cyan" + colors.blue + "key, looks like it would go in a fancy door lock")

    treasure_palace = dungeon.get_room("The Treasure Palace")
    treasure_palace.add_item("Gold", "A stack of gold bars. You can barely manage to pick it up, but a cart eases the load.")
    treasure_palace.add_item("Silver", "A pile of shiny silver coins. A mirror made of silver is")
    treasure_palace.add_item("Diamonds", "A string of diamond that can be worn like a tennis braclet.")
    treasure_palace.add_gold(10)

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
        direction = direction + "downward"

    if not room.doors:
        print("You are trapped, there are no doors")
    else:
        print(colors.orange + "There is a door leading " + direction)


def above_ground(dungeon, turns):
    if turns <= 3:
        dungeon.add_trap_door("The Lake-Mere", "The Cave", "d")
        if turns == 3:
            print("The opening below is slowly closing.")
        if turns == 0:
            dungeon.delete_trap_door("The Forest", "The Cave", "d")
    elif 3 < turns <= 6:
        dungeon.add_trap_door("The Farm", "The Cave", "d")
        if turns == 6:
            print("The opening below is slowly closing.")
        if turns == 4:
            dungeon.delete_trap_door("The Lake-Mere", "The Cave", "d")
    elif 6 < turns <= 9:
        dungeon.add_trap_door("Roadside", "The Cave", "d")
        if turns == 9:
            print("The opening below is slowly closing.")
    elif turns == 7:
        dungeon.delete_trap_door("The Farm", "The Cave", "d")
    else:
        dungeon.add_trap_door("The Forest", "The Cave", "d")
        if turns == 12:
            print("The opening below is slowly closing.")
        if turns == 10:
            dungeon.delete_trap_door("Roadside", "The Cave", "d")


def get_menu():
    return """
n - go north
s - go south
e - go east
w - go west
u - go upward
d - go downwards
l - look more closely
t - take all
i - inventory
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
            dungeon.add_trap_door("The Cave", "The Lake-Mere", "u")
        elif 3 < turns <= 6:
            dungeon.delete_trap_door("The Cave", "The Lake-Mere", "u")
            dungeon.add_trap_door("The Cave", "The Farm", "u")
        elif 6 < turns <= 9:
            dungeon.delete_trap_door("The Cave", "The Farm", "u")
            dungeon.add_trap_door("The Cave", "Roadside", "u", locked=True, unlock="key")
            print("The alarm clock is ringing loudly and shaking.")
        else:
            dungeon.delete_trap_door("The Cave", "The Roadside", "u")
            dungeon.add_trap_door("The Cave", "The Forest", "u")

        find_doors(current_room)
        ans = input(colors.default + """> """)
        reply = ""
        if ans == "debug":
            print(current_room)
        if ans == "help":
            reply = get_menu()
        elif ans == "e" or ans == "w" or ans == "n" or ans == "s" or ans == "u" or ans == "d":
            if dungeon.walk(current_room, ans, inventory) is not None:
                current_room = dungeon.walk(current_room, ans, inventory)
        elif ans == "ask" and current_room.people:
            current_room.people[0].ask()
        elif ans == "l" or ans == "look":
            reply = colors.blue + "You look more closely and see"
            if not current_room.items:
                reply = reply + " nothing"
            for item in current_room.items:
                reply = reply + "\n" + item
        elif ans == "take" or ans == "t":
            if current_room.items:
                reply = colors.blue + "You take the items in the room:"
            else:
                reply = "There are no items in the room to take."
            for item in current_room.items:
                reply = reply + "\n" + item
                inventory.append(item)
            if item in current_room.items:
                current_room.items.pop(item)

        elif ans == "i":
            reply = "Your bag contains:"
            for item in inventory:
                reply = reply + " " + item
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
            if item == "clock":
                print(colors.cyan + "The alarm clock reads: " + str(turns) + ":00 O'Clock")
        outside = ["The Roadside", "The Lake-Mere", "The Forest", "The Farm"]

        if current_room.name in outside:
            above_ground(dungeon, turns)

        if current_room.people:
            print(str(current_room.people[0].name) + " is here.")

        if current_room.name == "Roadside":
            print("There you are!' they say. 'I've been looking for you for " + str(
                turns + 1) + "hours!!! 'Let's get out of here, this place is giving me the creeps.'\nYou escaped. "
                             "\n \n" + colors.green + "THE END.")


# TODO add monsters
# hungry lion, have to give meat to get away


play()
