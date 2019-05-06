"""
    Implementation of a graph data structure
"""


class Node:
    def __init__(self,data):
        self.data=data
class Edge:
    def __init__(self,node1,node2):
        self.node1=node1
        self.node2=node2

class Graph:
    def __init__(self):
        self.arr=[None][None]
    def addnode(self,item):
        self.arr[0][1]=Node(item)
    def edge(self):
        arr1=[]
        arr1.append(Edge())

