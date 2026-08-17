class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n={}
        for ind,val in enumerate(nums):
            need=target-val
            if need in n:
                return [n[need],ind]
            n[val]=ind