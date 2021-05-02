from Graph import *
from pprint import pprint
if __name__ == "__main__":
    print("Testing")
    g=Graph.from_csv("Graph.csv")
    print(g)
    g.plot()