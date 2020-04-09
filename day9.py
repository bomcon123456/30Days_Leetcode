import itertools


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def get_char_backward(s):
            deleted_char = 0
            for c in reversed(s):
                # If we delete a char, increment counter
                if c == '#':
                    deleted_char += 1
                # If we see a character but saw a backspace
                elif deleted_char:
                    deleted_char -= 1
                # If we see a character and never saw backspace before
                else:
                    yield c
        # Check each char (a-z) whether match or not
        # Iterator -> O(1) space
        return all(x == y for x, y in itertools.zip_longest(get_char_backward(S), get_char_backward(T)))

    def ONspace_backspaceCompare(self, S: str, T: str) -> bool:
        s_a = []
        s_b = []
        for c in S:
            if c != "#":
                s_a.append(c)
            elif c == "#" and s_a:
                s_a.pop()
        for c in T:
            if c != "#":
                s_b.append(c)
            elif c == "#" and s_b:
                s_b.pop()
        if len(s_a) != len(s_b):
            return False
        else:
            for i in range(len(s_a)):
                if s_a[i] != s_b[i]:
                    return False
            return True
