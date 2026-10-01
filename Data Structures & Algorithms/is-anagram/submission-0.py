class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        # using dictonary for frequency mapping

        #first check the length of the 2 strings for early return
        if len(s) != len(t):
            return False
        
        count_s = {} # empty frequency look up dictionary
        count_t = {}

        for i in range(len(s)):

            count_s[s[i]] = 1 + count_s.get(s[i], 0) # initialize with default value of 0 and increment it by 1 if it exists in the dict
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        
        return count_s == count_t # return a boolean True/ False if the frequncy dicts are the same