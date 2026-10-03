class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #sliding window concept
        charSet = set() #to store the chars on their first appearance, holds the elements of the sliding window
        l = 0 #to track the start of the sliding window
        res = 0 # to hold the length of the substring 

        for r in range(len(s)):
            while s[r] in charSet: #duplicate is found in the set
                charSet.remove(s[l]) #remove the element found in the sliding window
                l = l + 1 #progress the window
        
            charSet.add(s[r]) #add the element to the set
            res = max(res, r - l + 1) #store the max between the last known size of the longest sliding window without duplicates
    
        return res

        