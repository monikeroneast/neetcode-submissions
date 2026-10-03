class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #using bucket sort algo
        count = {} #hashmap to store the frequency of the element
        freq = [[] for i in range(len(nums) + 1)] #array which has the indices as the frequency of occurences and element at the indices in the element that occurs at that many times (0-6 where 6 is the length of nums)

        #traverse through the array to get the frequency
        for num in nums:
            count[num] = 1 + count.get(num, 0) #get the frequency from the dict for the element num, if num is not there then default value is 0
        #update the frequency array using the dictionary
        for n, c in count.items():
            freq[c].append(n) #add the element to the frequency array at the relevant count indices location

        res = [] #empty list to store the element with max frenquency
        for i in range(len(freq) - 1, 0, -1): #iterate the frequeny array from the end in steps of 1
            for n in freq[i]: #if an element is found with a given frequency add it to the list result
                res.append(n)
                if len(res) == k: # the length of the result is at most 'k' element long
                    return res
        