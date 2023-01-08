class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_account=0
        for i in accounts:
            temp_value=0
            for j in i:
                temp_value+=j
            if temp_value>max_account:
                max_account=temp_value
        return max_account
