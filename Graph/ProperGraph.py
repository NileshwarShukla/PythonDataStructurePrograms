from enum import Enum
from collections import OrderedDict

class State(Enum):
    unvisited=1
    visited=2
    visiting=3


class Node:
    def __init__(self,num):
        self.num=num
        self.vs=State.unvisited
        self.adjacent=OrderedDict()

    def __str__(self):
        return str(self.num)

class Graph:

    def __init__(self):
        self.nodes=OrderedDict()

    def add_node(self,num):
        node=Node(num)
        self.nodes[num]=node
        return node
    def add_edge(self,f,t,wt=0):
        if f not in self.nodes:
            self.add_node(f)
        if t not in self.nodes:
            self.add_node(t)
        self.nodes[f].adjacent[self.nodes[t]]=wt
        
