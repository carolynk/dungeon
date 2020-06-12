import colors
from rooms import Map, Item
# from rooms import Person, Inventory

inventory = []

def create_dungeon():
    dungeon = Map()
    
    # Create Rooms
    dungeon.add_room("The sidewalk", "you are standing in front of an abandoned building.")
    dungeon.add_room("The lobby", "You are standing in a dark room with a high ceiling, with cobwebs EVERYWHERE.")
    dungeon.add_room("The switchboard", "There is old fashioned telephone swtichboard here, covered in cobwebs.")
    dungeon.add_room("The first hidden room", "This room has purple walls and a mysterious key card with a booth and a -100 sign on it.")
    dungeon.add_room("the second hidden room", "This room has orange walls and a mysterious smashed painting of a man the wall.")
    dungeon.add_room("THE BOOTH", "This is some sort of elevator, there seems to be a slot for a key card...")
    dungeon.add_room("-100 years ago_lobby", "The lobby 100 years ago")
    
    # Add doors
    dungeon.add_door("The sidewalk", "The lobby", "n")
    # The lobby
    dungeon.add_door("The lobby", "The switchboard", "e")
    dungeon.add_door("The lobby", "THE BOOTH", "n")

    dungeon.add_door("THE BOOTH", "-100 years ago_lobby", "s", locked = True, unlock = "Key Card 01" )
    # Add hiddendoor
    dungeon.add_door("The switchboard", "The first hidden room", "d", hidden=True)
    dungeon.add_door("The first hidden room", "the second hidden room", "w", hidden=True)

    # Add Items
    hidden_room = dungeon.get_room("The first hidden room")
    card01 = Item("Key card 01", "A key card with a booth and a -100 sign on it.")
    hidden_room.items["Key Card 01"] = card01

    hidden_room2 = dungeon.get_room("the second hidden room")
    card02 = Item("Key card 02", "A key card with a booth and a Wooly Mammoth sign on it.")
    hidden_room2.items["Key Card 02"] = card02


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
    print(colors.green + """Welcome.""" 
    + colors.pink + "\n(You can type " + colors.default + "help" 
    + colors.pink + " anytime to see options.)\n")
    current_room = dungeon.rooms["The sidewalk"]
    print(colors.green + current_room.name)
    print(colors.pink + current_room.description)
    if current_room.people:
        print(str(current_room.people[0].name) + " is here.")
    turns = 1
    while ans != 'q':
        if turns % 2 == 0:
          dungeon.add_door("The Cave", "The Lake-Mere", "u")
        else:
          dungeon.add_door("The Cave", "The Farm", "u")
        find_doors(current_room)
        ans = input(colors.default + """> """)
        reply = ""
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
            current_room.items = {}
        elif ans == "i":
            reply = colors.blue + "Your bag contains:"
            for item in inventory:
                reply = reply + " " + item
        elif ans == "q":
            exit()
        else:
            reply = "I don't understand. You can type help to see options."


        print("")
        print(colors.green + current_room.name + "\n" + colors.pink + current_room.description)
        if reply:
          print(reply)
        if current_room.people:
            print(str(current_room.people[0].name) + " is here.")

play()
