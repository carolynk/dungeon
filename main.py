import mylib
import colors
from rooms import Room, Person, Map


def create_dungeon():
    dungeon = Map()
    dungeon.add_room("The Hole", "You have fallen down a hole into a dungeon.")
    dungeon.add_room("The Cave", "A dark cave. You can't see anything.")
    falls = Room("Underground falls.", "A waterfall rushes from the ceiling.")
    farm = Room("The Farm",
                "Stairs lead to a light doorway. You the realize it is aboveground! Then cows, sheep, and some chicken signat it is a farm.")
    bunker = Room("The Bunker",
                  "A long room with dozens of bunkbeds line the walls. They look long abandoned. Cobwebs are everywhere.")
    control = Room("The Control center",
                   "There are three giant panels here with blinking lights and hundreds of knobs and buttons. There is what looks like a pilot seat facing a wide screen.")

    dungeon.add_door("The Hole", "The Cave", "e")
    # hole.doors['e'] = cave
    # cave.doors['n'] = falls
    # falls.doors['s'] = farm
    # farm.doors['n'] = bunker
    # bunker.doors['w'] = control

    return dungeon


def find_doors(room):
    """
    Parameters
    ----------
    room: Room
      where the player currently is
    """
    escape = True
    if 'e' in room.doors:
        direction = "east"
    elif 'w' in room.doors:
        direction = "west"
    elif 'n' in room.doors:
        direction = "north"
    elif 's' in room.doors:
        direction = "south"
    else:
        escape = False
    if escape:
        print(colors.orange + "There is a door to the " + direction)
    else:
        print("There are no doors")

def get_menu():
    return """
n - go north
s - go south
e - go east
w - go west
ask - ask the person a question
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
        ans = input("""\nWhat do you want to do? (type help to see options.) """)
        reply = " "
        if ans == "help":
            reply = get_menu()
        elif ans == "e" or ans == "w" or ans == "n" or ans == "s":
            if dungeon.walk(current_room, ans) is not None:
                current_room = dungeon.walk(current_room, ans)
            reply = colors.green + current_room.name + "\n" + colors.pink + current_room.description
        elif ans == "ask" and current_room.people:
            current_room.people[0].ask()
        elif ans == "q":
            exit()
        else:
            reply = "I don't understand."

        print(reply)
        if current_room.people:
            print(str(current_room.people[0].name) + " is here.")


play()
