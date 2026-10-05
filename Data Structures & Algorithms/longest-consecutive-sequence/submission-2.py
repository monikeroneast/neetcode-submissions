class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #check using the previous element of the sequence belongs to the set
        #initialize the set
        numSet = set(nums)
        longest = 0 #length of the subsequence

        #iterate through the set
        for num in numSet:
            #check if the previous element is in the set
            if (num - 1) not in numSet: #start of sequence
                length = 1
                #at the current element check, if there are consecutive element in the set
                while (num + length) in numSet: 
                    length = length + 1 #length's initial value is 1
                longest = max(longest, length)
        return longest

        