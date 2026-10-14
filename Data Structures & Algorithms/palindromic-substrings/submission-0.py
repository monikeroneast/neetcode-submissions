class Solution:
    def countSubstrings(self, s: str) -> int:
        #find substrings and check palindromes n keep a counter for the palindromes
        palindrome_count = 0

        def palindrome_substring(left: int, right: int) -> str:
            count = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            return count

        #traverse through the string
        for i in range(len(s)):
            #odd length palindromes with 1 center
            palindrome_count += palindrome_substring(i, i)
            #even length palindromes with 2 center
            palindrome_count += palindrome_substring(i, i + 1)
        
        return palindrome_count

        