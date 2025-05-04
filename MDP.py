#
#
#
#
#



class MDPNode:
    def __init__(self, id: int, rest: str, hw: str, time: str, actions: list, reward: list, transition: list, terminal = False):
        self.id = id
        self.rest_state = rest
        self.hw_state = hw
        self.time_state = time
        self.actions = actions
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
    
    def insert_children(self, child: list):
        for i in range(len(child)):
            self.children.append(child[i])

    def print_info(self):
        print(f'{self.rest_state}{self.hw_state} {self.time_state}')
    


def create_tree():
    root = MDPNode(0, "R", "U", "8p", ["P", "R", "S"], [2, 0, -1], [1.0, 1.0, 1.0])
    child1 = MDPNode(1, "T", "U", "10p", ["P", "R"], [2, 0], [1.0, 1.0])
    child2 = MDPNode(2, "R", "U", "10p", ["P", "R", "S"], [2, 2, 0, -1], [.5, .5, 1.0, 1.0])
    child3 = MDPNode(3, "R", "D", "10p", ["P", "R"], [2, 2, 0], [.5, .5, 1.0])
    root.insert_children([child1, child2, child3])
    child4 = MDPNode(4, "R", "U", "8a", ["P", "R", "S"], [2, 0, -1], [1.0, 1.0, 1.0])
    child7 = MDPNode(7, "R", "U", "10a", ["P", "R", "S"], [0, 0, 0], [1.0, 1.0, 1.0])
    child1.insert_children([child7, child4])
    child5 = MDPNode(5, "R", "D", "8a", ["P", "R"], [2, 0], [1.0, 1.0])
    child2.insert_children([child4, child7, child4, child5])
    child8 = MDPNode(8, "R", "D", "10a", ["P", "R", "S"], [4, 4, 4], [1.0, 1.0, 1.0])
    child3.insert_children([child5, child8, child5])
    child6 = MDPNode(6, "T", "U", "10a", ["P", "R", "S"], [-1, -1, -1], [1.0, 1.0, 1.0])
    child4.insert_children([child6, child7, child8]) 
    child9 = MDPNode(9, "T", "D", "10a", ["P", "R", "S"], [3, 3, 3], [1.0, 1.0, 1.0])
    child5.insert_children([child9, child8])
    class_node = MDPNode(10, "", "", "11a", [], [], [], True)
    for child in [child6, child7, child8, child9]:
        child.insert_children([class_node, class_node, class_node])
    return root
