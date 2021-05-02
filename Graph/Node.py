import math

# definition of the class that will contain all the nodes information
class Node:
    def __init__(self, Name='', Segments=[], Xcoordinate=0.0, Ycoordinate=0.0, Neighbors=[]):
        """Constructor of the Node class: generates a node instance

        Args:
            Name (str, optional): Name of the Node. Defaults to ''.
            Segments (list, optional): list of segments conected to the node. Defaults to [].
            Xcoordinate (float, optional): X coordinate. Defaults to 0.0.
            Ycoordinate (float, optional): Y coordinate. Defaults to 0.0.
            Neighbors (list, optional): List of nodes connected. Defaults to [].
        """        self.Name = Name
        self.Segments = Segments
        self.Xcoordinate = Xcoordinate
        self.Ycoordinate = Ycoordinate
        self.Neighbors = next

    # definition of the function that will add nodes as neighbours in case they aren't already
    def addNeighbor(n, nd):
        """adds Node to the list of Neightbors

        Args:
            n (int): position in the list of Neightbors
            nd (Node): Node to add

        Returns:
            bool: True if the operation was successful
        """        
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