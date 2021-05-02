#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Graph import *

""" ===========================================================================================
    Programa de pruebas del grafo.
"""
def crearGrafo ():
    G = Graph.Graph()
    Graph.addNode(G, node.Node("A", 1, 20))
    Graph.addNode(G, node.Node("B", 8, 17))
    Graph.addNode(G, node.Node("C", 15, 20))
    Graph.addNode(G, node.Node("D", 18, 15))
    Graph.addNode(G, node.Node("E", 2, 4))
    Graph.addNode(G, node.Node("F", 6, 5))
    Graph.addNode(G, node.Node("G", 12, 12))
    Graph.addNode(G, node.Node("H", 10, 3))
    Graph.addNode(G, node.Node("I", 19, 1))
    Graph.addNode(G, node.Node("J", 13, 5))
    Graph.addNode(G, node.Node("K", 3, 15))
    Graph.addNode(G, node.Node("L", 4, 10))
    Graph.addSegment(G, "A", "B")
    Graph.addSegment(G, "A", "E")
    Graph.addSegment(G, "A", "K")
    Graph.addSegment(G, "B", "A")
    Graph.addSegment(G, "B", "C")
    Graph.addSegment(G, "B", "F")
    Graph.addSegment(G, "B", "K")
    Graph.addSegment(G, "B", "G")
    Graph.addSegment(G, "C", "D")
    Graph.addSegment(G, "C", "G")
    Graph.addSegment(G, "D", "G")
    Graph.addSegment(G, "D", "H")
    Graph.addSegment(G, "D", "I")
    Graph.addSegment(G, "E", "F")
    Graph.addSegment(G, "F", "L")
    Graph.addSegment(G, "G", "B")
    Graph.addSegment(G, "G", "F")
    Graph.addSegment(G, "G", "H")
    Graph.addSegment(G, "I", "D")
    Graph.addSegment(G, "I", "J")
    Graph.addSegment(G, "J", "I")
    Graph.addSegment(G, "K", "A")
    Graph.addSegment(G, "K", "L")
    Graph.addSegment(G, "L", "K")
    Graph.addSegment(G, "L", "F")
    return G

def testGraph ():
    G = crearGrafo()
    # graph.plot(G)


print "Probando el grafo..."
testGraph()
print "OK"
