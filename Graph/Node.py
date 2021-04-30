import math

#definition of the class that will contain all the nodes information
class Node:
    def __init__(self):
        self.Name = ""
        self.Xcoordinate = 0.0
        self.Ycoordinate = 0.0
        self.Neighbors = []

#definition of the function that will add nodes as neighbours in case they aren't already
def addNeighbor(n,nd):
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

#function that will compute the euclidean distance from one node to another 
def distance(n1, n2):
    dist = math.sqrt((n2.Xcoordinate - n1.Xcoordinate)**2 + (n2.Ycoordinate - n1.Ycoordinate)**2)
    return dist
