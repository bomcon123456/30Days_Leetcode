class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            res = 0
            while n:
                a = n % 10
                res += a * a
                n = n//10
            if res == 1:
                return True
            elif res in seen:
                return False
            else:
                seen.add(res)
                n = res
        return False
