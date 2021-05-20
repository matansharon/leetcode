class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res=''
        for i in range(0,len(command)):
            if command[i]=='G':
                res+='G'
            if command[i]=='(' and command[i+1]==')':
                res+='o'
            if command[i]=='a':
                res+='al'
        return res
