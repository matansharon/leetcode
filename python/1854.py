# You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

# The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.

# Return the earliest year with the maximum population.

 

# Example 1:

# Input: logs = [[1993,1999],[2000,2010]]
# Output: 1993
# Explanation: The maximum population is 1, and 1993 is the earliest year with this population.
# Example 2:

# Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
# Output: 1960
# Explanation: 
# The maximum population is 2, and it had happened in years 1960 and 1970.
# The earlier year between them is 1960.


class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        max_alive=0
        min_year=9999
        max_year=0
        res=0
        for i in logs:
            if i[0]<min_year:
                min_year=i[0]
            if i[1]>max_year:
                max_year=i[1]
        for year in range(min_year,max_year):
            temp_max=0
            for log in logs:
                if year>=log[0] and year<log[1]:
                    temp_max+=1
            if temp_max>max_alive:
                
                max_alive=temp_max
                res=year
                
        return res
