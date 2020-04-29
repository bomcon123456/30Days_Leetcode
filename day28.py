import collections
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.arr = []
        self.dict = collections.defaultdict(int)
        for i in nums:
            self.add(i)

    def showFirstUnique(self) -> int:
        while self.arr and self.dict[self.arr[0]] > 1:
            self.arr.pop(0)
        if not self.arr:
            return -1
        else:
            return self.arr[0]

    def add(self, value: int) -> None:
        if value not in self.dict:
            self.arr.append(value)
        self.dict[value] += 1
