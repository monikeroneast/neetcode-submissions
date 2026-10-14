class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Solves House Robber II by splitting the circular neighborhood into 
        two linear sub-problems (ignoring the last house vs ignoring the first house).
        Returns the maximum profit between both scenarios.
        Time Complexity: O(N), Space Complexity: O(1)
        """

        if len(nums) == 1:
            return nums[0]

        def max_amount(nums: List[int]) -> int:
            """
            Calculates the maximum rob profit for a linear row of houses.
            Uses a sliding window tracking two previous states (prev1, prev2)
            to greedily select the maximum profit at each step.
            """
            n = len(nums)
            #base cases:
            prev2 = 0 #arriving at house i to rob after robbing house i - 2 back
            prev1 = 0 #arriving at house i after skipping house i - 1

            for num in nums:
                curr = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = curr

            return prev1

        return max(max_amount(nums[:-1]), max_amount(nums[1:]))

    
        