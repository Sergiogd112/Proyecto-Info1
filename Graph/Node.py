import math

# definition of the class that will contain all the nodes information
class Node:
    def __init__(self, Name='', Segments=[], Xcoordinate=0.0, Ycoordinate=0.0, Neighbors=[]):
        self.Name = Name
        self.Segments = Segments
        self.Xcoordinate = Xcoordinate
        self.Ycoordinate = Ycoordinate
        self.Neighbors = next

    # definition of the function that will add nodes as neighbours in case they aren't already
    def addNeighbor(n, nd):
        i = 0
        found = False
        while i < len(n.Neighbors) and not found:
            if n.Neighbors[i] == nd:
                found = True
            i += 1
        if not found:
            n.Neighbors.append(nd)
            return True
        else:
            return False
    def __repr__(self):
        return self.Name+f' ({self.Xcoordinate},{self.Ycoordinate})'
    # function that will compute the euclidean distance from one node to another
