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

    def optimal_policy(self, tree: MDP.MDPNode):
        curr_state = tree
        while curr_state.terminal != True:
            curr_state.print_info()
            action = np.argmax(self.q_table[curr_state.id])
            if len(curr_state.actions) != len(curr_state.rewards):
                if curr_state.actions[action] == "P":
                    _, t = curr_state.getedges()
                    choice = random.choices([curr_state.children[0], curr_state.children[1]], weights=[t[0], t[1]], k=1)
                    curr_state = choice[0]
                else:
                    curr_state = curr_state.children[action + 1]
            else:
                curr_state = curr_state.children[action]
        curr_state.print_info()
                    

    def simulate(self, tree: MDP.MDPNode):
        run = True
        episodes = 0
        while run:
            curr_state = tree
            old_q_table = self.q_table.copy()
            while curr_state.terminal != True:
                if random.random() < self.epsilon:
                    action = random.randint(0, (len(curr_state.actions) - 1))
                else:
                    action = np.argmax(self.q_table[curr_state.id])

                if len(curr_state.actions) != len(curr_state.rewards):
                    if curr_state.actions[action] == "P":
                        r, t = curr_state.getedges()
                        choice = random.choices([curr_state.children[0], curr_state.children[1]], weights=[t[0], t[1]], k=1)
                        for j in range(len(curr_state.children)):
                            if curr_state.children[j] == choice[0]:
                                break
                        reward = r[j]
                        next_state = choice[0]
                    else:
                        next_state = curr_state.children[action + 1]
                        reward = curr_state.rewards[action + 1]
                else:
                    next_state = curr_state.children[action]
                    reward = curr_state.rewards[action]

                print(f"Previous value: {self.q_table[curr_state.id, action]}")
                self.q_table[curr_state.id, action] += self.learning_rate * (reward + self.discount_factor*np.max(self.q_table[next_state.id]) - self.q_table[curr_state.id, action])
                print(f"New Value: {self.q_table[curr_state.id, action]}")
                print(f"Immediate Reward: {reward}")
                print(f"Q-values for next state: {self.q_table[next_state.id]}")
                curr_state = next_state
            diff = np.max(np.abs(old_q_table - self.q_table.copy()))
            episodes += 1
            if diff < 0.001:
                run = False
        
        print('-------------------------------------\n')
        print(f"Num episodes: {episodes}")
        print(self.q_table)
        self.optimal_policy(tree)
