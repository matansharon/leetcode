
class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        _min=min(salary)
        _max=max(salary)
        salary.pop(salary.index(_min))
        # print salary
        salary.pop(salary.index(_max))
        # print salary
        return sum(salary)/float(len(salary))
