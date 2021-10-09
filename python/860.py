# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

# Note that you don't have any change in hand at first.

# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with correct change, or false otherwise.

 

# Example 1:

# Input: bills = [5,5,5,10,20]
# Output: true
# Explanation: 
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.
# Example 2:

# Input: bills = [5,5,10,10,20]
# Output: false
# Explanation: 
# From the first two customers in order, we collect two $5 bills.
# For the next two customers in order, we collect a $10 bill and give back a $5 bill.
# For the last customer, we can not give change of $15 back because we only have two $10 bills.
# Since not every customer received correct change, the answer is false.
# Example 3:

# Input: bills = [5,5,10]
# Output: true
# Example 4:

# Input: bills = [10,10]
# Output: false
 

# Constraints:

# 1 <= bills.length <= 105
# bills[i] is either 5, 10, or 20.



class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change={5:0,10:0,20:0}
        
        if bills[0]!=5:
            return False
        i=0
        while len(bills)>0:
            b=bills.pop(0)
            if b==5:
                change[5]+=1
            elif b==10:
                if change[5]==0:
                    return False
                elif change[5]>0:
                    change[5]-=1
                    change[10]+=1
                    
            elif b==20:
                if change[10]==0 and change[5]<3:
                    return False
                elif change[10]>0 and change[5]==0:
                    return False
                elif change[10]>0 and change[5]>0:
                    change[10]-=1
                    change[5]-=1
                elif change[10]==0 and change[5]>2:
                    change[5]-=3
                
        return True
        