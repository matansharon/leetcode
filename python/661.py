import math
class Solution(object):
    def get_3X3(self,i,j,img):
        res=[]
        for i in range(i,i+3):
            temp=img[i]
            temp=temp[j:j+3]
            res.append(temp)
        return res
    def convert_to_grey(self,grid):
        p0=grid[0][0]
        p1=grid[0][1]
        p2=grid[0][2]
        p3=grid[1][0]
        p4=grid[1][2]
        p5=grid[1][2]
        p6=grid[2][0]
        p7=grid[2][1]
        p8=grid[2][2]
        r0=int(math.floor((p0+p1+p3+p4)/4))
        r1=int(math.floor((p0+p1+p2+p3+p4+p5)/6))
        r2=int(math.floor((p4+p1+p2+p5)/4))
        r3=int(math.floor((p0+p1+p3+p4+p6+p7)/6))
        r4=int(math.floor((p0+p1+p2+p3+p4+p5+p6+p7+p8)/9))
        r5=int(math.floor((p1+p2+p4+p5+p6+p7)/6))
        r6=int(math.floor((p3+p4+p6+p7)/4))
        r7=int(math.floor((p3+p4+p5+p6+p7+p8)/6))
        r8=int(math.floor((p5+p4+p7+p8)/4))
        
        
        res=[[r0,r1,r2],[r3,r4,r5],[r6,r7,r8]]
        return res
    
    def copy_to_original(self,small,large,x,y):
        large[x][y]=small[0][0]
        large[x][y+1]=small[0][1]
        large[x][y+2]=small[0][2]
        large[x+1][y]=small[1][0]
        large[x+1][y+1]=small[1][1]
        large[x+1][y+2]=small[1][2]
        large[x+2][y]=small[2][0]
        large[x+2][y+1]=small[2][1]
        large[x+2][y+2]=small[2][2]
        return large
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        #[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
        cnt=1
        grid=[]
        for i in range(5):
            row=[]
            for j in range(5):
                row.append(cnt)
                cnt+=1
            grid.append(row)
        for row in grid:
            print row
        print '**************************'
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                temp_s=self.get_3X3(i,j,grid)
                temp_s=self.convert_to_grey(temp_s)
                grid=self.copy_to_original(temp_s,grid,i,j)
                print grid
                
