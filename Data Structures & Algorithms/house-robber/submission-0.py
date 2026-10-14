class Solution:
    def rob(self, nums: List[int]) -> int:
        #house 0 -> nums[0] money
        #house 0, house 1, house 2 ...
        #check max money at each house to decide to rob or skip
        #base case -> generalize 
        #h0 = nums[0] #start at house0, money = nums[0] = 1 -> step 2 early
        #h1 = nums[1] #start at house1, coming from house0 not robbed, money = nums[1] = 1 -> step 1 early 
        #initialize
        n = len(nums)
        #if only house 1
        if n == 1:
            return nums[0]
        #h = [0] * n
        #base cases
        #h[0] = nums[0]
        #h[1] = max(nums[0], nums[1])
        prev2 = nums[0] #step 0
        prev1 = max(nums[0], nums[1]) #step 1 max(nums[0], nums[1])
        #for i in range(2, n):
        for i in range(2, n):
           #at every house i, robbing it implies came from skipping house(i - 1) or skipping house i which implies house(i - 2)
            #h[i] = max(h[i - 1], h[i - 2] + nums[i])
            curr = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = curr

        #return h[n - 1]
        return prev1
        