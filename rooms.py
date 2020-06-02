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
        self.doors = {}
        self.items = []
        self.people = []
    
    def add_neighbor(self, dir):
        self.doors.add(dir)

    def walk(self, direction):
        if direction in self.doors:
            new_room = self.doors[direction]
            return new_room
        else:
            print("You can't go that way.")

class Map:
    def __init__(self, rooms={}):
        """
        Make a map
        """
        self.rooms = rooms

    def add_room(self, name):
        new_room = Room(name)
        self.rooms[name] = new_room

    def get_room(self, name):
        if name in self.rooms.keys():
            return self.nodelist[name]
        return None

    def add_oneway_door(self, fr, to):
        if self.get_room(fr) is None:
            self.add_room(fr)
        if self.get_room(to) is None:
            self.add_room(to)
        self.get_room(fr).add_neighbor(to)
  



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
      print(self.answers[int(ans)-1])
      print("\n")
