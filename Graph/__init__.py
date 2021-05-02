from .Node import Node
from .Segment import Segment
from matplotlib import pyplot as plt
import math


class Graph:
    def __init__(self, nodes=[], segments=[], table=None, name="Noname"):
        """Constructor for the Graph class

        Args:
            nodes (Node Iterable, optional): Iterable of the nodes that form the Graph. Defaults to [].
            segments (Segment Iterable, optional): Iterable of the segments that form the Graph. Defaults to [].
            table (list, optional): Table of adjency of the graph. Defaults to None.
            name (str, optional): Name. Defaults to "Noname".
        """
        self.name = name
        self.nodes = nodes
        self.segments = segments
        if table:
            self.table = table
        else:
            self.table = self.generate_table()

    def add_node(self, node):
        """Adds a node to the Graph and updates the segments

        Args:
            node (Node): Node
        """
        self.nodes.append(node)
        self.segments.append(node.segments)

    def generate_table(self):
        """generate the table of adjency base on the list of nodes and segments in case it is not provided"""
        table = []
        grouped_segments = {}
        for segment in self.segments:
            try:
                grouped_segments[segment.origin.Name][
                    segment.destination.Name
                ] = segment.cost
            except:
                grouped_segments[segment.origin.Name] = {
                    segment.destination.Name: segment.cost
                }
        for node in self.nodes:
            costs = []
            dest = grouped_segments[node.Name].keys()
            for n in nodes:
                if n.Name in dest:
                    costs.append(grouped_segments[node.Name][n.Name])
                else:
                    costs.append(None)
            table.append([node] + costs)
        self.table = table

    def from_table(table):
        """Generates a graph from a table of adjency

        Args:
            table (list): table of adjency with structure node,x,y,..cost to nth node of destination...

        Returns:
            Graph: Graph based on the table of adjency
        """
        names = [line[0] for line in table]
        gnodes = []
        gsegments = []
        for line in table:
            if "unk" in line:
                segments = [
                    Segment(origin=line[0], destination=dest, cost=float(cost))
                    if cost != "unk"
                    else Segment(origin=line[0], destination=dest)
                    for dest, cost in zip(names, line[3:])
                    if cost != None
                ]
            gnodes.append(
                Node(
                    line[0],
                    segments,
                    Xcoordinate=line[1],
                    Ycoordinate=line[2],
                    Neighbors=[
                        neig for neig, cost in zip(names, line[3:]) if cost != None
                    ],
                )
            )
            gsegments.append(segments)
        return Graph(gnodes, gsegments, table)

    def from_csv(fileName):
        """Generates a graph based on a csv file with the same format as the table

        Args:
            fileName (str): filename of the csv file

        Returns:
            Graph: generated Graph
        """
        with open(fileName, "r") as f:
            data = [x.split(",") for x in f.read().split("\n")]
        gnodes = []
        gsegments = []
        table = []
        for line in data[1:]:
            segments = [
                Segment(origin=line[0], destination=dest, cost=float(cost))
                if cost != "unk" and cost != "None"
                else Segment(
                    origin=line[0],
                    destination=dest,
                    orgcoords=(float(line[1]), float(line[2])),
                    destcoords=(float(data[n + 1][1]), float(data[n + 1][2])),
                )
                if cost != "None"
                else None
                for n, (dest, cost) in enumerate(zip(data[0][3:], line[3:]))
            ]
            gnodes.append(
                Node(
                    Name=line[0],
                    Segments=segments,
                    Xcoordinate=float(line[1].replace("None", "-1")),
                    Ycoordinate=float(line[2].replace("None", "-1")),
                    Neighbors=[
                        neig
                        for neig, cost in zip(data[0][3:], line[3:])
                        if cost != "None"
                    ],
                )
            )
            table.append(
                [gnodes[-1]]
                + [
                    segment.cost if segment else None
                    for segment, cost in zip(segments, line[3:])
                ]
            )
            gsegments += [segment for segment in segments if segment]

        return Graph(gnodes, gsegments, table)

    def get_dict(self):
        """Generates a dictionary based on the graph
            Not finished

        Returns:
            dict: dict of the graph
        """
        graph_dict = {}
        names = [node.name for node in self.nodes]
        for node in self.nodes:
            neighbors = {}
            for neightbor in node.neighbors:
                for segment in node.segments:
                    if segment.origin == node.name and segment.origin == neightbor.name:
                        cost = segment.cost
                        break
                else:
                    cost = None
                neighbors[neightbor.name] = {"cost": cost}
            graph_dict[node.name] = {"x": node.x, "y": node.y, "neightbors": neightbors}
        return graph_dict

    def __repr__(self):
        return (
            f"{self.name}'s table of adjancy:\n["
            + ",\n".join([x.__repr__() for x in self.table])
            + "]"
        )

    def plot(self):
        """Displays the graph using matplotlib
        Not finished
        """
        plt.plot(
            [node.Xcoordinate for node in self.nodes],
            [node.Ycoordinate for node in self.nodes],
            "o",
        )
        [plt.text(node.Xcoordinate, node.Ycoordinate, node.Name) for node in self.nodes]
        [
            (
                plt.arrow(
                    line[0].Xcoordinate,
                    line[0].Ycoordinate,
                    dest.Xcoordinate - line[0].Xcoordinate,
                    dest.Ycoordinate - line[0].Ycoordinate,
                ),
                plt.text(
                    line[0].Xcoordinate
                    + 0.25 * (dest.Xcoordinate - line[0].Xcoordinate),
                    line[0].Ycoordinate
                    + 0.25 * (dest.Ycoordinate - line[0].Ycoordinate),
                    str(round(seg, 2)),
                ),
            )
            for line in self.table
            for seg, dest in zip(line[3:], self.nodes)
            if seg
        ]
        plt.show()
