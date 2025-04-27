import Q_learning
import MDP



q = Q_learning.Q_learning(0.1, 0.99, 0.2)
tree = MDP.create_tree()
q.simulate(tree)
