class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(filter(str.isalnum, s)).lower()
        if word == word[::-1]:
            return True
        else:
            return False