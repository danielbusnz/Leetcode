class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = Counter(nums)
        highest_key = max(count, key=count.get)
        return highest_key