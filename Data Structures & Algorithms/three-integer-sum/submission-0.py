class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #sort the list
        nums.sort()
        result = [] #empty list

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: #duplicate fixed element so skipped
                continue
            target = -nums[i] #sum of the other 2 left and right should be negative of the fixed element so that triplet sum is 0
            left, right = i + 1, len(nums) - 1 #left element will start after the fixed element
            while left < right:
                s = nums[left] + nums[right] #sum of left and right element
                if s == target:
                    result.append([nums[i], nums[left], nums[right]])
                    #duplicate check and skip for both the sides
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right -1]:
                        right = right - 1
                    left = left + 1
                    right = right - 1
                elif s < target:
                    left = left + 1
                else: 
                    right = right - 1
           
        return result        