class Solution(object):
    def every_possible_sequence(self,word):
        res=set()
        for len1 in range(1,len(word)):
            for start in range(0,len(word)):
                res.add(word[start:start+len1])
        res.add(word)
        
        return res
            
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        זה הפתרון היפה שלי שבודק על כל רצף שקיים ולא רק בהתחלה
        """
        res=''
        temparr=[]
        for i in strs:
            temparr.append(len(i))
        min_len=min(temparr)
        arr=self.every_possible_sequence(strs[0])
        for i in arr:
            all_=True
            for j in strs:
                if i not in j:
                    all_=False
            if all_ and len(i)>len(res):
                res=i
        return res
            
