#
#
#
#
#

import numpy as np


class MDPNode:
    def __init__(self, rest: str, hw: str, time: str, reward: list, transition: list, terminal = False):
        self.rest_state = rest
        self.hw_state = hw
        self.time_state = time
        self.rewards = reward
        self.transition_prob = transition
        self.terminal = terminal
        self.children = []

    def isterminal(self):
        if self.time_state == "11a" or self.terminal == True:
            return True
        else:
            return False
    
    def getedges(self):
        return self.rewards, self.transition_prob
    
    def create_child(self, possible_moves: list):
        self.children = possible_moves
    
    
class MDPGraph:
    def __init__(self, root):
        self.root = root

    def insert_children(self, curr: MDPNode, child: MDPNode, action: str):
        pass

def create_tree():
    root = MDPNode("R", "U", "8p", [2, 0, -1], [1.0, 1.0, 1.0])
    root.create_child([1, 1, 1])
    tree = MDPGraph(root)
    child1 = MDPNode("T", "U", "10p", [2, 0, None], [1.0, 1.0, None])
    child2 = MDPNode("R", "U", "10p", [0, [2, 2], -1], [1.0, [.5, .5], 1.0])
    child3 = MDPNode("R", "D", "10p", [0, [2, 2], None], [1.0, [.5, .5], None])
    tree.insert_children(tree.root, None, 0)