states = ['RU8p', 'TU10p', 'RD10p', 'RU10p', 'RU8a', 'RD8a', 'TU10a', 'RU10a', 'RD10a', 'TD10a', '11a']
actions = ['Party', 'Rest', 'Study', 'any']

# for each state
available_actions = {
    'RU8p': ['Party', 'Rest', 'Study'],
    'TU10p': ['Party', 'Rest'],
    'RD10p': ['Party', 'Rest'],
    'RU10p': ['Party', 'Rest', 'Study'],
    'RU8a': ['Party', 'Rest', 'Study'],
    'RD8a': ['Party', 'Rest'],
    'TU10a': ['any'],
    'RU10a': ['any'],
    'RD10a': ['any'],
    'TD10a': ['any'],
    # this one is the terminal state for all
    '11a': []
}


# Transition probabilities and rewards -> (initial_state, action):(next_state, probability, reward)
transitions = {
    # RU8p
    ('RU8p', 'Party'): [('TU10p', 1.0, 2)],
    ('RU8p', 'Rest'): [('RU10p', 1.0, 0)],
    ('RU8p', 'Study'): [('RD10p', 1.0, -1)],

    # TU10p
    ('TU10p', 'Party'): [('RU10a', 1.0, 2)],
    ('TU10p', 'Rest'): [('RU8a', 1.0, 0)],

    # RD10p
    ('RD10p', 'Party'): [('RD8a', 0.5, 2), ('RD10a', 0.5, 2)],
    ('RD10p', 'Rest'): [('RD8a', 1.0, 0)],

    # RU10p
    ('RU10p', 'Party'): [('RU8a', 0.5, 2), ('RU10a', 0.5, 2)],
    ('RU10p', 'Rest'): [('RU8a', 1.0, 0)],
    ('RU10p', 'Study'): [('RD8a', 1.0, -1)],

    # RU8a
    ('RU8a', 'Party'): [('TU10a', 1.0, 2)],
    ('RU8a', 'Rest'): [('RU10a', 1.0, 0)],
    ('RU8a', 'Study'): [('RD10a', 1.0, -1)],

    # RD8a
    ('RD8a', 'Party'): [('TD10a', 1.0, 2)],
    ('RD8a', 'Rest'): [('RD10a', 1.0, 0)],

    # TU10a
    ('TU10a', 'any'): [('11a', 1.0, -1)],

    # RU10a
    ('RU10a', 'any'): [('11a', 1.0, 0)],

    # RD10a
    ('RD10a', 'any'): [('11a', 1.0, 4)],

    # TD10a
    ('TD10a', 'any'): [('11a', 1.0, 3)],
}

state_values = {state: 0.0 for state in states}

def value_iteration(discount:float, threshold:float):
    iteration = 1
    while True:
        diff = 0
        print(f"Iteration {iteration}")
        for state in states:
            # skip the terminal state at the end
            if state == '11a':
                continue
            action_values = {}
            for action in available_actions.get(state, []):
                value = 0
                for (next_state, prob, reward) in transitions.get((state, action), []):
                    value += prob * (reward + discount * state_values[next_state])
                action_values[action] = value
            
            if action_values:
                max_action = max(action_values, key=action_values.get)
                max_value = action_values[max_action]
                old_value = state_values[state]
                state_values[state] = max_value

                print(f"State: {state} | Old Value: {old_value:.4f} | New Value: {max_value:.4f}")
                print(f"Action Values: {action_values}")
                print(f"Selected Action: {max_action}\n")

                diff = max(diff, abs(old_value - max_value))

        iteration += 1
        if diff < threshold:
            break
    
    print(f"Num of iterations: {iteration}")
    print("Final policy (values and best actions for each state)")
    for state in states:
        action_values = {}
        for action in available_actions.get(state, []):
            value = 0
            for (next_state, prob, reward) in transitions.get((state, action), []):
                value += prob * (reward + discount * state_values[next_state])
            action_values[action] = value
        if action_values:
            best_action = max(action_values, key=action_values.get)
            print(f"{state}: {state_values[state]:.4f} | Best action: {best_action}")