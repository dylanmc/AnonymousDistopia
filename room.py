import json

def get_room(id):
    ret = None
    with open(str(id)+".json", "r") as r:
        jsontext = r.read()
        d = json.loads(jsontext)
        d['id'] = id
        ret = Room (**d)
        print ret
    return ret

class Room():
    def __init__(self, id=0, name= "Room #1", description= "An empty room", neighbors={}):
        self.id = id
        self.name = name
        self.description = description
        self.neighbors = neighbors

    def __repr__(self):
        ret = self.description + '...' + self.name + '\n'
        exits = ""
        anyExits = False
        for d in self.neighbors:
            anyExits = True
            exits += d + ', '
        if anyExits:
            ret = ret + "You see exits to the " + exits
        return ret

    def getNeighbor(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

    def north(self):
        return self._neighbor('n')

    def east(self):
        return self._neighbor('e')

    def south(self):
        return self._neighbor('s')

    def west(self):
        return self._neighbor('w')
