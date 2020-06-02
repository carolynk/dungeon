import mylib
import colors
from rooms import Room, Person, Map


def make_rooms():
    hole = Room("The Hole", "You have fallen down a hole into a dungeon.")
    cave = Room("The Cave", "A dark cave. You can't see anything.")
    falls = Room("Underground falls.", "A waterfall rushes from the ceiling.")
    farm = Room("The Farm", "Stairs lead to a light doorway. You the realize it is aboveground! Then cows, sheep, and some chicken signat it is a farm.")
    bunker = Room("The Bunker", "A long room with dozens of bunkbeds line the walls. They look long abandoned. Cobwebs are everywhere.")
    control = Room("The Control center", "There are three giant panels here with blinking lights and hundreds of knobs and buttons. There is what looks like a pilot seat facing a wide screen.")

    hole.doors['e'] = cave
    cave.doors['n'] = falls
    falls.doors['s'] = farm
    farm.doors['n'] = bunker
    bunker.doors['w'] = control


    return map



def find_doors(room):
    """
    Parameters
    ----------
    room: Room
      where the player currently is
    """
    if 'e' in room.doors:
      dir = "east"
    elif 'w' in room.doors:
      dir = "west"
    elif 'n' in room.doors:
      dir = "north"
    elif 's' in room.doors:
      dir = "south"
    else:
        print("There are no doors")
        dir = "nowhere"
    print(colors.orange + "There is a door to the: " + dir)



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
    # inventory = []
    map = Map()
    current_room = map.rooms[1]
    print(colors.green + current_room.name)
    print(colors.pink + current_room.description)
    if current_room.people:
      print(str(current_room.people[0].name) + " is here.")
    while ans != 'q':
        find_doors(current_room)
        print(colors.default)
        ans = input("""\nWhat do you want to do? (type help to see options.) """)
        if ans == "help":
            reply = get_menu()
        elif ans == "e" or ans == "w" or ans == "n" or ans == "s":
            if current_room.walk(ans) is not None:
                current_room = current_room.walk(ans)
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
        print(" ")

play()





