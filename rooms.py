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
        doors = name:direction
        """
        self.name = name
        self.description = desc
        self.items = []
        self.doors = {}
        self.people = []

    def add_neighbor(self, neighbor_name, direction):
        self.doors[direction] = neighbor_name


class Map:
    def __init__(self, rooms=None):
        """
        Make a map

        """
        if not rooms:
            rooms = {}
        self.rooms = rooms

    def add_room(self, name, desc=""):
        new_room = Room(name, desc)
        self.rooms[name] = new_room

    def get_room(self, name):
        if name in self.rooms.keys():
            return self.rooms[name]
        return None

    def add_trap_door(self, fr, to, direction):
        """
        A directed edge between rooms
        """
        if self.get_room(fr) is None:
            self.add_room(fr)
        if self.get_room(to) is None:
            self.add_room(to)
        self.get_room(fr).add_neighbor(to, direction)

    def add_door(self, id1, id2, direction):
        mirror = {"e": "w", "w": "e", "n": "s", "s": "n"}
        self.add_trap_door(id1, id2, direction)
        self.add_trap_door(id2, id1, mirror[direction])

    def walk(self, fr, direction):
        if fr.doors[direction]:
            new_room = self.get_room(fr.doors[direction])
            return new_room
        else:
            print("You can't go that way.")


class Person:
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
