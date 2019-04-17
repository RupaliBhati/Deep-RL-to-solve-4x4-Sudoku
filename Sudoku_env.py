from gym import spaces
import numpy as np
from copy import deepcopy


class SudokuEnv():

    def __init__(self):
        #self.action_space = spaces.Discrete(4)    # inside the brackets, specify the number of actions
        self.state = [0,3,4,0,4,0,0,2,1,0,0,3,0,2,1,0]   #initialise the state
        
        # Start the first round
        self.reset()
        
    def empty_positions(self, state):     #returns list of locations of empty positions on the grid
        emp_pos = []
        for ix in range(len(state)):
            if state[ix]==0:
                emp_pos.append(ix)
        return emp_pos

    def get_action(self, state):
        possible_locations = self.empty_positions(state)
        loc = np.random.choice(possible_locations)
        action = np.random.choice(range(1,5))
        return (action,loc)

    def transition(self, state, action):    #state is an array, action is tuple (number, location)
        new_state = deepcopy(state)         #to avoid in-place substitution
        act = action[0]
        loc = action[1]
        new_state[loc] = act
        return new_state

    def reward(self, action, next_state):        
        '''
        MAX_X = MAX_Y = 4
        
        grid = np.arange(16).reshape([4,4])
        it = np.nditer(grid, flags=['multi_index'])
        while not it.finished:
            s = it.iterindex
            y, x = it.multi_index
    
            if action[1] == s:
                if x == 0:

            it.iternext()
        '''

        if action[1]==0:            #if location == 0
            if action[0] in (next_state[1],next_state[2],next_state[3],next_state[4],next_state[8],next_state[12]): 
            #if next_state[1] == action[0] or next_state[2] == action[0] or next_state[3] == action[0]:  
                r = -10
            else:
                r=0
        elif action[1]==1:            #if location == 1
            if action[0] in (next_state[0],next_state[2],next_state[3],next_state[5],next_state[9],next_state[13]): 
                r = -10
            else:
                r=0       
        elif action[1]==2:            #if location == 2
            if action[0] in (next_state[0],next_state[1],next_state[3],next_state[6],next_state[10],next_state[14]): 
                r = -10
            else:
                r=0  
        elif action[1]==3:            #if location == 3
            if action[0] in (next_state[0],next_state[1],next_state[2],next_state[7],next_state[11],next_state[15]): 
                r = -10
            else:
                r=0     
        elif action[1]==4:            #if location == 4
            if action[0] in (next_state[5],next_state[6],next_state[7],next_state[0],next_state[8],next_state[12]): 
                r = -10
            else:
                r=0 
        elif action[1]==5:            #if location == 5
            if action[0] in (next_state[4],next_state[6],next_state[7],next_state[1],next_state[9],next_state[13]): 
                r = -10
            else:
                r=0     
        elif action[1]==6:            #if location == 6
            if action[0] in (next_state[4],next_state[5],next_state[7],next_state[2],next_state[10],next_state[14]): 
                r = -10
            else:
                r=0          
        elif action[1]==7:            #if location == 7
            if action[0] in (next_state[4],next_state[5],next_state[6],next_state[3],next_state[11],next_state[15]): 
                r = -10
            else:
                r=0       
        elif action[1]==8:            #if location == 8
            if action[0] in (next_state[9],next_state[10],next_state[11],next_state[0],next_state[4],next_state[12]): 
                r = -10
            else:
                r=0 
        elif action[1]==9:            #if location == 9
            if action[0] in (next_state[8],next_state[10],next_state[11],next_state[1],next_state[5],next_state[13]): 
                r = -10
            else:
                r=0     
        elif action[1]==10:            #if location == 10
            if action[0] in (next_state[8],next_state[9],next_state[11],next_state[2],next_state[6],next_state[14]): 
                r = -10
            else:
                r=0          
        elif action[1]==11:            #if location == 11
            if action[0] in (next_state[8],next_state[9],next_state[10],next_state[3],next_state[7],next_state[15]): 
                r = -10
            else:
                r=0    
        elif action[1]==12:            #if location == 12
            if action[0] in (next_state[13],next_state[14],next_state[15],next_state[0],next_state[4],next_state[8]): 
                r = -10
            else:
                r=0 
        elif action[1]==13:            #if location == 13
            if action[0] in (next_state[12],next_state[14],next_state[15],next_state[1],next_state[5],next_state[9]): 
                r = -10
            else:
                r=0     
        elif action[1]==14:            #if location == 14
            if action[0] in (next_state[12],next_state[13],next_state[15],next_state[2],next_state[6],next_state[14]): 
                r = -10
            else:
                r=0          
        elif action[1]==15:            #if location == 15
            if action[0] in (next_state[12],next_state[13],next_state[14],next_state[3],next_state[7],next_state[11]): 
                r = -10
            else:
                r=0                                                       
        return r


    def step(self, state, action):   
        #assert self.action_space.contains(action)  
        current_state = deepcopy(state)                               #to avoid in-place substitution

        next_state = self.transition(current_state, action)       #next_state
        reward1 = self.reward(action, next_state)

        return next_state, reward1


    def reset(self):
        return self.state