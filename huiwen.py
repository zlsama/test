import re
class Solution(object):
    def isPalindrome(self, s):
        if len(s)==0:
            return True
        self.s=s
        s1=re.findall('\w+',self.s)
        s2=''.join(s1)
        s2=s2.upper()
        if s2==s2[::-1]:
            return True
        else:
            return False