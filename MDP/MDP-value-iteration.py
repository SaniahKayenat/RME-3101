grid = [
    [0,0,0,1],
    [0,None,0,-1],
    [0,0,0,0]
]
row = 3
col = 4
#noise 0.2
noise = 0.2
noise = noise/2
gamma = 0.9 #discount
probability = 0.8
living_reward  = 0
terminal_states = [(0,3),(1,3)]
actions = ['U','D','L','R']
def reward(state):
    i,j = state
    return grid[i][j]

def is_terminal(state):
    i,j = state
    if (i,j) in terminal_states:
        return True
    return False
def is_none(state):
    i,j = state
    if i == 1  and j == 1:
        return True
    return False


def normalize(t):
    p_sum = sum(t.values())
    for transition in t:
        t[transition]/=p_sum
    return t
def possible_next_states(state):
    i,j = state
    possible_nxt_states = [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]
    if i == 0:
        possible_nxt_states.remove((i-1,j))
    if j == 0:
        possible_nxt_states.remove((i,j-1))
    if i == row-1:
        possible_nxt_states.remove((i+1,j))
    if j == col -1:
        possible_nxt_states.remove((i,j+1))

    for m,n in possible_nxt_states:
        if is_none((m,n)):
            possible_nxt_states.remove((m,n))
            break
    return possible_nxt_states

def transition_probability(state,action):
    i,j = state
    transitions = {}
    if action == 'U':
        transitions = {(i-1,j): probability,(i,j+1):noise,(i,j-1):noise}
    elif action == 'D':
        transitions =  {(i+1, j): probability, (i, j+1): noise, (i, j-1): noise}
    elif action == 'L':
        transitions =  {(i, j-1): probability, (i-1, j): noise, (i+1, j): noise}
    elif action == 'R':
        transitions =  {(i, j+1): probability, (i-1, j): noise, (i+1, j): noise}

    possible_transitions = possible_next_states((i,j))
    temp = transitions.copy()
    for transition in temp:
        if transition not in possible_transitions:
            del transitions[transition]
    
    final_transitions = normalize(transitions)
    return final_transitions
    
def q_value(state):
    q_value_dict = {}
    
    for action in actions:
        q_val = 0
        transitions = transition_probability(state,action)
        for transition in transitions:
            x,y = transition
            if (x>=0 and x<row) and (y>=0 and y<col):
                q_val+= transitions[transition]*gamma*grid[x][y]
        q_value_dict[action] = q_val
    return q_value_dict

def value_policy(state):
    value_dict = q_value(state)
    #print(value_dict)
    value_list = list(value_dict.values())
    #print(value_list)
    key_list = list(value_dict.keys())
    #print(key_list)
    max_val = max(value_list)
    #print(max_val)
    position = value_list.index(max_val)
    return (max_val,key_list[position])

action_grid = [[0]*col for i in range(row)]
threshold = .0000001

while True:
    cnt = 0
    for i in range(row):
        for j in range(col):
            if is_terminal((i,j)) or is_none((i,j)):
                continue
            else:
                curr_val = grid[i][j]
                new_val,new_pos = value_policy((i,j))
                if curr_val<new_val:
                    action_grid[i][j] = new_pos
                    grid[i][j] = new_val
                if abs(new_val-curr_val) < threshold:
                    cnt+=1
    if cnt == 9:
        break
    
    
for i in range(row):
    for j in range(col):
        if is_terminal((i,j)) or is_none((i,j)):
            print(grid[i][j],end='')
            print("    ",end='')
            continue
        else:
            print(grid[i][j],end='')
            print(",",end='')
            print(action_grid[i][j],end='')
            print("  ",end='')
    print('\n')

# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np


# numpy_grid = np.array(grid)
# numpy_action_grid = np.array(action_grid)
  

# formatted_text = (np.asarray(["{0}\n{1:.2f}".format(numpy_action_grid, numpy_grid) for numpy_action_grid, numpy_grid in zip(numpy_action_grid.flatten(), numpy_grid.flatten())])).reshape(3, 4)

# # drawing heatmap
# fig, ax = plt.subplots()
# colormap = sns.color_palette("Purples") 
# ax = sns.heatmap(numpy_grid, annot=formatted_text, fmt="", cmap=colormap)

# plt.show()
 








