class Solution(object):
    def lengthOfLastWord(self, s):
        list=s.split()
    
        res = len(list[-1])
        return res
        