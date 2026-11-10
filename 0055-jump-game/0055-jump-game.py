class Solution:
    def canJump(self, nums: list[int]) -> bool:
        current = 0
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False
            
            farthest = max(farthest, nums[i]+ i)

            if farthest >= len(nums):
                return True
        return True