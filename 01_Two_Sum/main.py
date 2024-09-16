from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pastNums = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in pastNums:
                return [i, pastNums[diff]]
            pastNums[val] = i
        return