

from board import *
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of the Eight Puzzle.
    """
  
    def  __init__(self, board, predecessor, move):
        
        self.board = board
        self.predecessor = predecessor 
        self.move = move 
        if predecessor is None:
            self.num_moves = 0
        else:
            self.num_moves = predecessor.num_moves + 1 

    def __repr__(self):
 
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False
    
    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        return True


    

    def is_goal(self):
 
        return self.board.tiles == GOAL_TILES
    
    def generate_successors(self):
        
        successors = []
        for move in MOVES:
            b = self.board.copy() 
            if b.move_blank(move):
                new_state = State(b, self, move)
                successors += [new_state]
        return successors
        
    def print_moves_to(self):
       
        if self.predecessor is None:    
            print('initial state:')
            print (self.board)
        else:
            self.predecessor.print_moves_to()
            print("move the blank " + self.move + ":")
            print(self.board)
        
        
        
        
        
        
        
        