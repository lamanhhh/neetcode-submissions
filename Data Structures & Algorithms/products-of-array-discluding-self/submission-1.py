class Solution:
    @staticmethod
    def pre(nums: list[int]):
        ret = [1] * len(nums)

        for i in range(1, len(nums)):
            ret[i] = ret[i - 1] * nums[i - 1]

        return ret
            
    @staticmethod
    def suf(nums: list[int]):
        ret = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            ret[i] = ret[i + 1] * nums[i + 1]

        return ret
        
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        return [a*b for a, b in zip(self.pre(nums), self.suf(nums))]