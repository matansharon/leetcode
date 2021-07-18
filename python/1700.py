class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        stop=len(students)       
        while stop>0:
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                stop=len(students)
            else:
                temp=students.pop(0)
                students.append(temp)
                stop-=1  
        return len(students)
