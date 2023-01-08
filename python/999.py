class Solution(object):
    def create_col(self,pos,board):
        col=[]
        for row in board:
            col.append(row[pos])
        return col
    def find_the_rook(self,board):
        row=0
        col=0
        for r in range(len(board)):
            if 'R' in board[r]:
                row=r
                col=board[row].index('R')
        return [row,col]
    def check_row(self,pos,row):
        res=0
        # checking to the left
        for i in range(pos,-1,-1):
            if row[i]=='p':
                res+=1
                break
            if row[i]=='B':
                break
        # checking to the right
        for i in range(pos,len(row)):
            if row[i]=='p':
                res+=1
                break
            if row[i]=='B':
                break
        return res
    # def check_column(pos,col):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        pos=self.find_the_rook(board)
        r=self.check_row(pos[1],board[pos[0]])
        temp_c=self.create_col(pos[1],board)
        c=self.check_row(pos[1],temp_c)
        return r+c
