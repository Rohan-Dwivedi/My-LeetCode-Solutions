class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        rev = 0
        if x < 0:
            return False
        while x > 0:
            rev = (rev * 10) + (x % 10)
            x //= 10
        if rev == n:
            return True
        return False