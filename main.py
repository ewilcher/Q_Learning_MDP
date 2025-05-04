import Q_learning
import MDP
import value_iteration

print('Value iteration\n')
print('-------------------------------------\n')
value_iteration.value_iteration(0.99,0.001)
print('-------------------------------------\n')


print('Q Learning\n')
print('-------------------------------------\n')
q = Q_learning.Q_learning(0.1, 0.99, 0.2)
tree = MDP.create_tree()
q.simulate(tree)
print('\n-------------------------------------')

