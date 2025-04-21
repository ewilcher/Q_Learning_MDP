#
#
#
#
#

import numpy as np


class MDPNode:
    def __init__(self, rest, hw, time, reward, transition, terminal = False):
        self.rest_state = rest
        self.hw_state = hw
        self.time_state = time
        self.rewards = reward
        self.transition_prob = transition
        self.terminal = terminal

    def isterminal(self):
        if self.time_state == "11a" or self.terminal == True:
            return True
        else:
            return False
    
    def getedges(self):
        return self.rewards, self.transition_prob
    
    
class MDPGraph:
    def __init__(self, root):
        self.root = root

    def insert_child(self, curr: MDPNode, child: MDPNode, action: str);
        pass

def create_tree():
    pass