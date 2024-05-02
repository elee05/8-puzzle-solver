

from searcher import *


def create_searcher():
    searcher = Searcher()
    return searcher

def eight_puzzle(init_boardstr):
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher()

    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()
            
def main():
    while True:
        init_boardstr = input('input puzzle sequence as digit string: ')
        
        if len(init_boardstr) == 9:
            if ('0' in init_boardstr and
                '1' in init_boardstr and 
                '2' in init_boardstr and
                '3' in init_boardstr and 
                '4' in init_boardstr and 
                '5' in init_boardstr and 
                '6' in init_boardstr and 
                '7' in init_boardstr and 
                '8' in init_boardstr):
                    print('please hold')
                    eight_puzzle(init_boardstr)
            else:
                print('wrong input')

           
        elif init_boardstr == 'cancel':
            break
        else:
            print('Wrong input')
        
    print('bye')
        

    