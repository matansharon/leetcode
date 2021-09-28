# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

# There are two types of logs:

# Letter-logs: All words (except the identifier) consist of lowercase English letters.
# Digit-logs: All words (except the identifier) consist of digits.
# Reorder these logs so that:

# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.
# Return the final order of the logs.

 

# Example 1:

# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
# Example 2:

# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]


class Solution(object):    
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        let=[]
        dig=[]
        res=[]
        for log in logs:
            l=log.split(' ',1)
            if l[1][0].isalpha():
                let.append(l)
            else:
                dig.append(l)
        for l in let:
            temp=l[0]
            l[0]=l[1]
            l[1]=temp
        let.sort()
        # print let
        lett=[]
        for l in let:
            st=l[1]+' '+l[0]
            lett.append(st)
        digg=[]
        for d in dig:
            st=d[0]+' '+d[1]
            digg.append(st)
        for i in lett:
            res.append(i)
        for i in digg:
            res.append(i)
        return res
            
