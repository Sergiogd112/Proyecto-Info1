import math


class Segment:
    def __init__(
        self, cost=None, origin=None, destination=None, orgcoords=None, destcoords=None
    ):
        """Constuctor for the segment class

        Args:
            cost (float, optional): Cost to travers the segment. Defaults to None.
            origin (str, optional): Name of the node of origin. Defaults to None.
            destination (str, optional): name of the node of destiny. Defaults to None.
            orgcoords (float tuple, optional): coordinates of the node of origin. Defaults to None.
            destcoords (float tuple, optional): coordinates of the node of destination. Defaults to None.
        """
        if cost != None and cost != "None" and cost != "unk":
            self.cost = cost
        else:
            self.cost = Segment.distance(orgcoords=orgcoords, destcoords=destcoords)
        self.origin = origin
        self.destination = destination

    def distance(n1=None, n2=None, orgcoords=None, destcoords=None):
        """Calculates the distance between two nodes or coordinates in the cartesian space

        Args:
            n1 (Node, optional): Node of origin. Defaults to None.
            n2 (Node, optional): Node of destination. Defaults to None.
            orgcoords (float tuple, optional): coordinates of origin. Defaults to None.
            destcoords (float tuple, optional): coordinates of destination. Defaults to None.

        Returns:
            float: distance between them in the cartesian space
        """
        if n1:
            dist = math.sqrt(
                (n2.Xcoordinate - n1.Xcoordinate) ** 2
                + (n2.Ycoordinate - n1.Ycoordinate) ** 2
            )
        else:
            dist = math.sqrt(
                (destcoords[0] - orgcoords[0]) ** 2
                + (destcoords[1] - orgcoords[1]) ** 2
            )
        return dist

    def __repr__(self):
        return f"{self.origin}-{self.cost}-{self.destination}"
