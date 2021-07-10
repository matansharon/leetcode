class Solution(object):
    def numSpecialEquivGroups(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        arr=[]
        arr2=[]
        res=0
        for word in words:
            odds=[]
            even=[]
            for i in range(len(word)):
                if i%2==0:
                    even.append(word[i])
                else:
                    odds.append(word[i])
            
            even.sort()
            odds.sort()
            arr.append([even,odds])
        
        print arr
        for i in arr:
            if i not in arr2:
                arr2.append(i)
        return len(arr2)
                    
                    
