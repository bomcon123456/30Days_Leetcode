class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.min_stack = []

    def push(self, x: int) -> None:
        if len(self.arr) == 0:
            self.min_stack.append(x)
        else:
            cur_min = self.min_stack[-1]
            if x < cur_min:
                self.min_stack.append(x)
            else:
                self.min_stack.append(cur_min)
        self.arr.append(x)

    def pop(self) -> None:
        if len(self.arr) > 0:
            self.min_stack.pop()
            self.arr.pop()

    def top(self) -> int:
        if len(self.arr) > 0:
            return self.arr[-1]

    def getMin(self) -> int:
        if len(self.arr) > 0:
            return self.min_stack[-1]


class MinStack_ConstantSpace:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.current_min = None

    def push(self, x: int) -> None:
        if len(self.arr) == 0:
            self.arr.append(x)
            self.current_min = x
        else:
            if x < self.current_min:
                self.arr.append(2*x - self.current_min)
                self.current_min = x
            else:
                self.arr.append(x)

    def pop(self) -> None:
        if len(self.arr) > 0:
            x = self.arr[-1]
            if x < self.current_min:
                self.current_min = 2*self.current_min - x
            self.arr.pop()

    def top(self) -> int:
        if len(self.arr) > 0:
            x = self.arr[-1]
            if x < self.current_min:
                return self.current_min
            else:
                return x

    def getMin(self) -> int:
        if len(self.arr) > 0:
            return self.current_min
