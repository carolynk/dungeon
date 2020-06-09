import colors


class Room:
    """
    Attributes
    ----------
    name: string
      name of the room
    description: string
      description of the room
    doors: string list
      list of directions (n,s,e,w)

    """

    def __init__(self, name, desc):
        """
        Make a room
        """
        self.name = name
        self.description = desc
        self.items = {}
        self.doors = {}  # direction: new room name
        self.hidden_doors = {}  # direction: new room name
        self.locked = {}  # direction: name of item that unlocks it
        self.people = []

    def add_neighbor(self, neighbor_name, direction, locked=False, unlock=""):
        self.doors[direction] = neighbor_name
        if locked:
            self.locked[direction] = unlock

    def delete_neighbor(self, direction):
        self.doors.pop(direction)

    def add_hidden_neighbor(self, neighbor_name, direction):
        self.hidden_doors[direction] = neighbor_name

    def add_item(self, name, desc=""):
        new_item = Item(name, desc)
        self.items[name] = new_item


class Map:
    def __init__(self, rooms=None):
        """
        Make a map

        """
        if not rooms:
            rooms = {} # name : room object
        self.rooms = rooms

    def add_room(self, name, desc=""):
        new_room = Room(name, desc)
        self.rooms[name] = new_room

    def get_room(self, name):
        if name in self.rooms.keys():
            return self.rooms[name]

    def add_trap_door(self, fr, to, direction, locked=False, unlock=""):
        """
        A directed edge between rooms
        """
        if self.get_room(fr) is None:
            self.add_room(fr)
        if self.get_room(to) is None:
            self.add_room(to)
        self.get_room(fr).add_neighbor(to, direction, locked, unlock)

    def delete_trap_door(self, fr, to, direction):
        """
        A directed edge between rooms
        """
        if self.get_room(fr) is None:
            self.add_room(fr)
        if self.get_room(to) is None:
            self.add_room(to)
        self.get_room(fr).delete_neighbor(direction)

    def add_hidden_trap_door(self, fr, to, direction):
        """
        A directed edge between rooms
        """
        if self.get_room(fr) is None:
            self.add_room(fr)
        if self.get_room(to) is None:
            self.add_room(to)
        self.get_room(fr).add_hidden_neighbor(to, direction)

    def add_door(self, id1, id2, direction, locked=False, unlock=""):
        mirror = {"e": "w", "n": "s", "u": "d"}
        mirror.update(dict((v, k) for (k, v) in mirror.items()))
        self.add_trap_door(id1, id2, direction, locked, unlock)
        self.add_trap_door(id2, id1, mirror[direction])



    def add_hidden_door(self, id1, id2, direction):
        mirror = {"e": "w", "w": "e", "n": "s", "s": "n", "u": "d", "d": "u"}
        self.add_hidden_trap_door(id1, id2, direction)
        self.add_trap_door(id2, id1, mirror[direction])

    def walk(self, fr, direction):
        if direction in fr.locked.keys():
            print("The door is locked.")
        elif direction in fr.doors.keys():
            new_room = self.get_room(fr.doors[direction])
            return new_room
        elif direction in fr.hidden_doors.keys():
            new_room = self.get_room(fr.hidden_doors[direction])
            return new_room
        else:
            print("You can't go that way.")


class NPC:
    """
    Attributes
    ----------
    name: string
      name of the person


    """

    def __init__(self, name, desc):
        """
        Make a room
        """
        self.name = name
        self.description = desc
        self.questions = []
        self.answers = []

    def ask(self):
        for q in self.questions:
            print(q)
        ans = input("What do you want to ask? ")
        print("\n" + colors.pink + self.name + " replies: ")
        print(self.answers[int(ans) - 1])
        print("\n")


class Item:
    """
    Attributes
    ----------
    name: string
      name of the person
    """

    def __init__(self, name, desc):
        """
        Make an item
        """
        self.name = name
        self.description = desc


class Player:
    def __init__(self, items=None):
        """
        Make an item
        """
        self.inventory = {}
        self.turns = 0

    def get_item(self, name):
        if name in self.inventory.keys():
            return self.inventory[name]

    def add_item(self, name):
        new_item = self.get_item(name)
        self.inventory[name] = new_item

