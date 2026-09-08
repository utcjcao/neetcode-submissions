class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input: integer array. 

        # pro tip: do edge cases last

        # output: integer array of length k, where each value is one of the kth
        # most common elements

        # clarifying questions:
        # 1. what happens if there are less elements than k? 
        # assume we still output less than k elems
        # 2. what happens if k is zero? don't return anything
        # 3. is there an integer limit on what can be in nums? 

        # start off with our frequency dict
        freq = {}

        # iterate through nums
        for n in nums:
        # add to the freq dict for each value in nums
            freq[n] = freq.get(n, 0) + 1

        # convert our dict to an array of tuples (key, value)
        freq_array = [(key, value) for key, value in freq.items()]
        # sort by the value
        freq_array = sorted(freq_array, key=lambda x: x[1])

        # we'll just return the kth top elements of our array
        return [elem[0] for elem in freq_array[len(freq)-k:]]
        # we can consider using a heap, but for now. we'll stick with just using a sorted freq array
        

        # time complexity: n, nlogn, O(nlogn)
        # space: O(n)
