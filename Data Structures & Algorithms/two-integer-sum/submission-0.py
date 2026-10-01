class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = [] # intialize an empty list to hold the index and value

        for i, value in enumerate(nums):
            result.append([value, i]) # (0:nums[0], 1:0)
        
        result.sort()

        left = 0
        right = len(nums) - 1

        while left < right:
            s = result[left][0] + result[right][0]
            if s == target:
                return [min(result[left][1], result[right][1]), # smaller index of the pair
                        max(result[left][1], result[right][1])] # larger index of the pair
            elif s < target:
                left = left + 1
            else:
                right = right - 1
        
        return []