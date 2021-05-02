import math


class Segment:
    def __init__(
        self, cost=None, origin=None, destination=None, orgcoords=None, destcoords=None
    ):
        if cost != None and cost != "None" and cost != "unk":
            self.cost = cost
        else:
            self.cost = Segment.distance(orgcoords=orgcoords, destcoords=destcoords)
        self.origin = origin
        self.destination = destination

    def distance(n1=None, n2=None, orgcoords=None, destcoords=None):
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
