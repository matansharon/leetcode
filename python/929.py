class Solution(object):
    def clean_the_adress(self,adress):
        local=''
        domain=''
        at=-1
        try:
            at=adress.index('@')
        except:
            at=-1
        if at!=-1:
            local=adress[:at]
            domain=adress[at+1:]
        temp=''
        for i in local:
            if i!='.':
                temp+=i
        local=temp
        
        try:
            pos=local.index('+')
            local=local[:pos]
        except:
            pass
        return local+'@'+domain
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        _set=set()
        for mail in emails:
            _set.add(self.clean_the_adress(mail))
        return len(_set)
