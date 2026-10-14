class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s: #empty string s
            return ""
        longest = ""
        def expand_from_center(left: int, right: int) -> str: # returns the substring

            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1: right]
        
        #odd length string would have 1 center odd palindromes and even length string would have 2 center even palindromes
        for i in range(len(s)):
            palindrome1 = expand_from_center(i, i)
            if len(palindrome1) > len(longest):
                longest = palindrome1
            
            palindrome2 = expand_from_center(i, i + 1)
            if len(palindrome2) > len(longest):
                longest = palindrome2
            
        return longest