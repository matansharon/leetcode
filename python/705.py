class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data=set()
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.data.add(key)
        
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        try:
            self.data.remove(key)
        except:
            pass
        
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.data
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
