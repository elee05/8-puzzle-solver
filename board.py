

# a 2-D list that corresponds to the tiles in the goal state

GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]


class Board:

    def __init__(self, digitstr):
        """
            input: digitstr is a permutation of the digits 0-9
        """
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        for i in range(3):
            for j in range(3):
                self.tiles[i][j] = digitstr[3 * i + j]
                if self.tiles[i][j] == "0":
                    self.blank_r = i
                    self.blank_c = j 

    def __repr__(self):
        """ returns a string representing Board object 
        """ 
        s = ""
        for i in self.tiles:
            for x in i:
                if x == "0":
                    s += "_ "
                
                else:
                    s += x + " "
            s += '\n'   

        return s               
    
    def move_blank(self, direction):
        """ moves in terms of blank space not actual tiles
        """
        new_row = 0
        new_col = 0
        
        if direction not in ["up", "down", "right", "left"]:
            return False
        
        if direction == "up":
            new_row = self.blank_r - 1
            new_col = self.blank_c
        
        elif direction == "down":
            new_row = self.blank_r + 1 
            new_col = self.blank_c
            
        elif direction == "right":
            new_row = self.blank_r
            new_col = self.blank_c + 1 
        
        elif direction == "left":
            new_row = self.blank_r
            new_col = self.blank_c - 1 
        
        if new_row < 0 or new_row > 2 or new_col < 0 or new_col > 2:
            return False
        
        elif new_row >= 0 and new_row <= 2 and new_col >= 0 and new_col <= 2:
            self.tiles[self.blank_r][self.blank_c] = self.tiles[new_row][new_col]
            self.tiles[new_row][new_col] = "0"
            self.blank_r = new_row
            self.blank_c = new_col
            return True 
        
        else:
            return False 
        
        
    def digit_string(self):
        
        s = ""
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[row])):
                s += str(self.tiles[row][col])
        return s 
        
    def copy(self):
        
        new_board = Board(self.digit_string())
        return new_board
        
    def num_misplaced(self):
        
        count = 0
        for i in range(3):
            for j in range(3):
                if self.tiles[i][j] != GOAL_TILES[i][j] and self.tiles[i][j] != "0":
                    count += 1 
        return count 
        
    def __eq__(self, other):
        
        if self.digit_string() == other.digit_string():
            return True 
        else:
            return False
        
        
        
        
        
        
        