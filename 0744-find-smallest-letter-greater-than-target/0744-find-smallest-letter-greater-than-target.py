class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        lo = 0
        hi = len(letters)

        while lo < hi:
            mid = (lo + hi) // 2
            if letters[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        
        return letters[lo % len(letters)]
        