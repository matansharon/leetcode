class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        for arr in image:
            temp_arr=reversed(arr)
            temp_arr2=[]
            for i in temp_arr:
                if i==0:
                    temp_arr2.append(1)
                else:
                    temp_arr2.append(0)
            res.append(temp_arr2)
        return res
