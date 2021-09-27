# Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

# Players take turns placing characters into empty squares ' '.
# The first player A always places 'X' characters, while the second player B always places 'O' characters.
# 'X' and 'O' characters are always placed into empty squares, never on filled ones.
# The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

# You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

 

# Example 1:


# Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# Output: "A"
# Explanation: A wins, they always play first.
# Example 2:


# Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# Output: "B"
# Explanation: B wins.
# Example 3:


# Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# Output: "Draw"
# Explanation: The game ends in a draw since there are no moves to make.
# Example 4:


# Input: moves = [[0,0],[1,1]]
# Output: "Pending"
# Explanation: The game has not finished yet.
 

# Constraints:

# 1 <= moves.length <= 9
# moves[i].length == 2
# 0 <= rowi, coli <= 2
# There are no repeated elements on moves.
# moves follow the rules of tic tac toe.



class Solution(object):
    def fill_the_grid(self,moves,grid):
        for i in range(len(moves)):
            move=moves[i]
            
            if i%2==0:
                grid[move[0]][move[1]]='X'
            else:
                grid[move[0]][move[1]]='O'
        return grid
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        grid=[]
        grid.append([' ']*3)
        grid.append([' ']*3) 
        grid.append([' ']*3) 
        grid=self.fill_the_grid(moves,grid)
        for row in grid:
            if row.count('X')==3:
                return 'A'
            if row.count('O')==3:
                return 'B'    
        for row in range(len(grid)):
            col=[]
            for c in range(len(grid)):
                col.append(grid[c][row])
            if col.count('X')==3:
                return 'A'
            if col.count('O')==3:
                return 'B'
        left_diagonal=[grid[0][0],grid[1][1],grid[2][2]]
        right_diagonal=[grid[0][2],grid[1][1],grid[2][0]]
        if right_diagonal.count('X')==3:
            return 'A'
        if right_diagonal.count('O')==3:
            return 'B'
        if left_diagonal.count('X')==3:
            return 'A'
        if left_diagonal.count('O')==3:
            return 'B'
        if len(moves)==9:
            return 'Draw'
        return 'Pending'
