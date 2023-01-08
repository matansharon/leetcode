class Solution(object):
    def get_upper_bound(self,pos,char_pos):
        for i in char_pos:
            if i>=pos:
                return i 
        return -1
    def get_bottom_bound(self,pos,char_pos):
        for i in reversed(char_pos):
            if i<=pos:
                return i
        return -1
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        char_pos=[]
        res=[]
        for i in range(len(s)):
            if s[i]==c:
                char_pos.append(i)
        for i in range(len(s)):
            d=self.get_bottom_bound(i,char_pos)
            u=self.get_upper_bound(i,char_pos)
            dis1=-1
            dis2=-1
            if d>-1:
                dis1=abs(i-d)
            if u!=-1:
                dis2=abs(u-i)
            if dis1==-1:
                res.append(dis2)
            elif dis2==-1:
                res.append(dis1)
            else:
                res.append(min(dis1,dis2))
        return res
