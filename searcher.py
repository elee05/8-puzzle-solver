

import random
from state import *

def h2(state):
    """ takes a State object called state 
    """
    log = []
    for r in range(len(state.board.tiles)):
        for c in range(len(state.board.tiles[0])):
            if state.board.tiles[r][c] != '0':
                if state.board.tiles[r][c] != GOAL_TILES[r][c]:
                    for R in range(len(state.board.tiles)):
                        for C in range(len(state.board.tiles[0])):
                            if GOAL_TILES[R][C] == state.board.tiles[r][c]:
                                log += [[state.board.tiles[r][c], r, c, R, C]]
    comb_dist = 0            
    for val in log:
        #comb_dist += (abs(val[1] - val[0]//3) + abs(val[2] - val[0])
        comb_dist += (abs(val[1] - val[3]) + abs(val[2] - val[4]))
                    
    return (comb_dist)


class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
    """
    
    def __init__(self):
        self.states = []
        self.num_tested = 0 
        
    def add_state(self, state): 
        self.states += [[self.priority(state), state]]
    
    def should_add(self, state):
        if state.creates_cycle():
            return False 
        else:
            return True 
        
    def add_states(self, new_states):
        for state in new_states:
            if self.should_add(state):
                self.add_state(state)
    
    def next_state(self):
        s = max(self.states)
        self.states.remove(s)
        return s[1]
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * (h2(state) + state.num_moves)

    def find_solution(self, init_state):
        """  performs a full state-space search that begins at the specified initial state init_state and ends when the goal state is found or when the Searcher runs out of untested states
        """
        self.add_state(init_state)
        while self.states:
            s = self.next_state()
            self.num_tested += 1 
            if s.is_goal():
                return s 
            else:
                self.add_states(s.generate_successors())
        return None 
        





