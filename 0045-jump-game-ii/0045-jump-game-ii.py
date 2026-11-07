class Solution:
    def jump(self, nums: list[int]) -> int:
        farthest = 0
        jumps = 0
        current_end = 0

        for i in range(len(nums)-1):
            if i > farthest:
                return False
            farthest = max(farthest, nums[i] + i)

            if current_end == i:
                current_end = farthest
                jumps += 1
        return jumps