class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_shift = 0
        n = len(s)
        for d, l in shift:
            if d == 0:
                total_shift += l
            else:
                total_shift -= l
        total_shift %= n
        return s[total_shift:] + s[:total_shift]
