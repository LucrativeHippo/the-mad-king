class Pos:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Pos(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Pos(self.x-other.x, self.y-other.y)

    def __abs__(self):
        return Pos(abs(self.x),abs(self.y))

    def __cmp__(self, other):
        return (self.x == other.x) & (self.y == other.y)

    def __eq__(self, other):
        return (self.x == other.x) & (self.y == other.y)

    def __repr__(self):
        return "("+str(self.x) + "," + str(self.y)+")"

    def __hash__(self):
        return hash((self.x,self.y))

    def distance_to(self, other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5
