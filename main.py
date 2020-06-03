import mylib
import colors
from rooms import Room, Person, Map, Item

inventory = []


def create_dungeon():
    dungeon = Map()
    
    # Create Rooms
    dungeon.add_room("The Hole", "You have fallen down a hole into a dungeon.")
    dungeon.add_room("The Cave", "A dark cave. You can't see anything.")
    dungeon.add_room("The Falls.", "An underground waterfall rushes from the ceiling.")
    dungeon.add_room("The Farm",
                "Stairs lead to a light doorway. You the realize it is aboveground! Then cows, sheep, and some chicken signat it is a farm.")
    dungeon.add_room("The Bunker",
                  "A long room with dozens of bunkbeds line the walls. They look long abandoned. Cobwebs are everywhere.")
    dungeon.add_room("The Control Center",
                   "There are three giant panels here with blinking lights and hundreds of knobs and buttons. There is what looks like a pilot seat facing a wide screen.")
    dungeon.add_room("The Inhouse",
                   "There are hundreds of toilets here. Some even with the carcus of fish, urine, and feces. Eww!")

    # Add doors
    dungeon.add_door("The Hole", "The Cave", "e")
    dungeon.add_door("The Cave", "The Farm", "n")

    # Control center doors
    dungeon.add_door("The Control Center", "The Cave", "e")
    dungeon.add_door("The Control Center", "The Falls", "n")
    dungeon.add_door("The Control Center", "The Bunker", "s")
    dungeon.add_door("The Control Center", "The Inhouse", "e")

    # Add Items
    hole = dungeon.get_room("The Hole")
    rope = Item("Rope", "A long, sturdy rope")
    hole.items.append(rope)

    hole = dungeon.get_room("The Hole")
    rope = Item("Rope", "A long, sturdy rope")
    hole.items.append(rope)

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
        direction = direction + " west"
    if 'n' in room.doors:
        direction = direction + " north"
    if 's' in room.doors:
        direction = direction + " south"

    if room.doors:
        print(colors.orange + "There is a door to the " + direction)
    else:
        print("There are no doors")



def get_menu():
    return """
n - go north
s - go south
e - go east
w - go west
l - look more closely
"""


def play():
    ans = ''
    dungeon = create_dungeon()
    current_room = dungeon.rooms["The Hole"]
    print(colors.green + current_room.name)
    print(colors.pink + current_room.description)
    if current_room.people:
        print(str(current_room.people[0].name) + " is here.")
    while ans != 'q':
        find_doors(current_room)
        print(colors.default)
        ans = input("""What do you want to do? (type help to see options.) """)
        print(" ")
        reply = " "
        if ans == "help":
            reply = get_menu()
        elif ans == "e" or ans == "w" or ans == "n" or ans == "s":
            if dungeon.walk(current_room, ans) is not None:
                current_room = dungeon.walk(current_room, ans)
            reply = colors.green + current_room.name + "\n" + colors.pink + current_room.description
        elif ans == "ask" and current_room.people:
            current_room.people[0].ask()
        elif ans == "l" or ans == "look":
            print(colors.green + current_room.name)
            print(colors.pink + current_room.description)
            reply = colors.blue + "You look more closely and see:"
            if not current_room.items:
                reply = reply + " nothing"
            for item in current_room.items:
                reply = reply + " " + str(item.name)
        elif ans == "take" or ans == "t":
            if current_room.items:
                reply = "You take the items in the room:"
            else:
                reply = "There are no items in the room to take."
            for item in current_room.items:
                reply = reply + " " + str(item.name)
                current_room.items.pop()
                inventory.append(item)
        elif ans == "i":
            reply = "Your bag contains:"
            for item in inventory:
                reply = reply + " " + item.name
        elif ans == "q":
            exit()
        else:
            reply = "I don't understand."

        print(reply)
        if current_room.people:
            print(str(current_room.people[0].name) + " is here.")


play()
