class Solution:
    def isHappy(self, n: int) -> bool:

        while n > 5: n = sum((int(i)) ** 2 for i in str(n))
        return True if n == 1 else False

