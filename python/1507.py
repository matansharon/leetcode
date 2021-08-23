# Given a date string in the form Day Month Year, where:

# Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
# Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
# Year is in the range [1900, 2100].
# Convert the date string to the format YYYY-MM-DD, where:

# YYYY denotes the 4 digit year.
# MM denotes the 2 digit month.
# DD denotes the 2 digit day.
 

# Example 1:

# Input: date = "20th Oct 2052"
# Output: "2052-10-20"
# Example 2:

# Input: date = "6th Jun 1933"
# Output: "1933-06-06"
# Example 3:

# Input: date = "26th May 1960"
# Output: "1960-05-26"


class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        res=''
        monthes=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']        
        Month={}
        temp=1
        for i in monthes:
            if temp<10:
                Month[i]='0'+str(temp)
            else: 
                Month[i]=str(temp)
            temp+=1
        
        arr=date.split(' ')
        d=arr[0]
        temp=''
        for i in d:
            if i.isdigit():
                temp+=i
        if int(temp)<10:
            d='0'+temp
        else:
            d=temp
        m=Month[arr[1]]
        y=arr[2]
        return y+'-'+m+'-'+d
        
