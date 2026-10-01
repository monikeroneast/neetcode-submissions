class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        best = 0 # best area
        left, right = 0, len(heights) - 1
        
        while left < right:
            w = right - left # width of the container
            h = min(heights[left], heights[right]) # constrained by the minimum of left and right side
            best = max(best, w * h) # area of the container
            if heights[left] < heights[right]: # search for height better than the last visited height
                left = left + 1
            else:
                right = right - 1

        return best