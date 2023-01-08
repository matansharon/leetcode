class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.ptr=0
        self.my_list=[]
        for i in range(0,n):
            self.my_list.append('')
        
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        temp_list=[]
        key=idKey-1
        self.my_list[key]=value
        
        if key==self.ptr:
            while self.ptr<len(self.my_list) and self.my_list[self.ptr]!='' :
                temp_list.append(self.my_list[self.ptr])
                self.ptr+=1
        return temp_list
        
                
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# print(obj.my_list)
# param_1 = obj.insert(idKey,value)
