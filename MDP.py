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
    
    
class MDPGraph:
    def __init__(self, root):
        self.root = root

    def insert_children(self, curr: MDPNode, children: list):
        for i in range(len(children)):
            curr.children.append(children[i])

def create_tree():
    root = MDPNode(0, "R", "U", "8p", ["P", "R", "S"], [2, 0, -1], [1.0, 1.0, 1.0])
    tree = MDPGraph(root)
    child1 = MDPNode(1, "T", "U", "10p", ["P", "R"], [2, 0], [1.0, 1.0])
    child2 = MDPNode(2, "R", "U", "10p", ["P", "R", "S"], [0, [2, 2], -1], [1.0, [.5, .5], 1.0])
    child3 = MDPNode(3, "R", "D", "10p", ["P", "R"], [[2, 2], 0], [[.5, .5], 1.0])
    tree.insert_children(tree.root, [child1, child2, child3])
    curr = tree.root.children[0]
    child4 = MDPNode(4, "R", "U", "10a", ["P", "R", "S"], [0, 0, 0], [1.0, 1.0, 1.0])
    child5 = MDPNode(5, "R", "U", "8a", ["P", "R", "S"], [2, 0, -1], [1.0, 1.0, 1.0])
    tree.insert_children(curr, [child4, child5])
    curr = tree.root.children[1]
    child6 = MDPNode(6, "R", "D", "8a", ["P", "R"], [2, 0], [1.0, 1.0])
    tree.insert_children(curr, [child5, [child5, child4], child6])
    curr = tree.root.children[2]
    child7 = MDPNode(7, "R", "D", "10a", ["P", "R", "S"], [4, 4, 4], [1.0, 1.0, 1.0])
    tree.insert_children(curr, [child6, [child6, child7]])
    curr = tree.root.children[1]
    curr = curr.children[0]
    child8 = MDPNode(8, "T", "U", "10a", ["P", "R", "S"], [-1, -1, -1], [1.0, 1.0, 1.0])
    tree.insert_children(curr, [child8, child4, child7])
    curr = tree.root.children[2]
    curr = curr.children[0]
    child9 = MDPNode(9, "T", "D", "10a", ["P", "R", "S"], [3, 3, 3], [1.0, 1.0, 1.0])
    tree.insert_children(curr, [child7, child9])
    class_node = MDPNode(10, "", "", "11a", [], [], [], True)
    curr = curr.children[0]
    tree.insert_children(curr, [class_node])
    curr = tree.root.children[2]
    curr = curr.children[0]
    curr = curr.children[1]
    tree.insert_children(curr, [class_node])
    curr = tree.root.children[0]
    curr = curr.children[0]
    tree.insert_children(curr, [class_node])
    curr = tree.root.children[1]
    curr = curr.children[0]
    curr = curr.children[0]
    tree.insert_children(curr, [class_node])
    return tree

