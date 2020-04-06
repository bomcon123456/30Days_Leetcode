import collections


class Solution:
    # O(NKlogK) with N word and K is length of word
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for word in strs:
            base = ''.join(sorted(word))
            d[base].append(word)

        return d.values()

    # O(NK)
    def better_solution(self, strs):
        d = collections.defaultdict(list)
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c) - ord('a')] += 1
            d[tuple(count)].append(word)
        return d.values()
