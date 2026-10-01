class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        # dictionary 
        look_up = set() # create an empty set that stores the unique num once they have been traversed

        for num in nums:
            if num in look_up:
                return True    # num exists in look_up so the current encounter is a duplicate
            look_up.add(num)   # when the num is not present in look_up it means the num is encountered for the first time and therefore is added to the look_up 
        
        return False