class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        canidate = None

        for num in nums:
            if count == 0:
                canidate = num
            
            if num == canidate:
                count += 1
            else:
                count -= 1
        return canidate      