class Solution:
    def isPalindrome(self, s: str) -> bool:
        #strip the spaces, lowercase, alphanumeric
        #s = ''.join(c.lower() for c in s if c.isalpha())
        clean_s = ''
        for c in s:
            if c.isalnum():
                clean_s = clean_s + c.lower()
        
        left = 0
        right = len(clean_s) - 1

        while left < right:
            if clean_s[left] != clean_s[right]:
                return False
        
            left = left + 1
            right = right - 1
        return True