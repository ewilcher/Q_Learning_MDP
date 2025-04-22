#
#
#
#
#

import numpy as np
import random
import MDP


class Q_learning:
    def __init__(self, lr, df, e, num_states=11, num_actions=3):
        self.q_table = np.zeros((num_states, num_actions))
        self.learning_rate = lr
        self.discount_factor = df
        self.epsilon = e

    def simulate(self, num_epochs, tree):
        for i in range(num_epochs):
            curr_state = tree.root
            while curr_state.terminal != True:
                if random.random() < self.epsilon:
                    action = random.randint(0, (len(curr_state.actions) - 1))
                else:
                    action = np.argmax(self.q_table[curr_state.id])
                    if action > (len(curr_state.actions) - 1):
                        action = random.randint(0, (len(curr_state.actions) - 1))
                print(len(curr_state.children))
                next_state = curr_state.children[action]
                if type(next_state) == list:
                    choice = random.choices(list(enumerate(next_state)), weights=curr_state.transition_prob, k=1)[0]
                    index, next_state = choice[0]
                    reward = curr_state.rewards[action]
                    reward = reward[index]
                else:
                    reward = curr_state.rewards[action]

                self.q_table[curr_state.id, action] += self.learning_rate *(reward + self.discount_factor*np.max(self.q_table[next_state.id]) - self.q_table[curr_state.id, action])
                curr_state = next_state
