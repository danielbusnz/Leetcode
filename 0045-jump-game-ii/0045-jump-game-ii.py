class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        farthest = 0
        current_end = 0

        for i in range(len(nums)-1):
            if i > farthest:
                return False
            
            farthest = max(farthest, nums[i] + i)

            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps