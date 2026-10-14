class Solution:
    def climbStairs(self, n: int) -> int:
        
        steps = n
        prev2 = 1 #Step[0] start
        prev1 = 1 #Step[1] start
        if n <= 1: # when n is 0/ 1
            return 1 
        for _ in range(2, steps + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return prev1
        