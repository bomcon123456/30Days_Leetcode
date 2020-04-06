import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for word in strs:
            base = ''.join(sorted(word))
            d[base].append(word)
        
        return d.values()