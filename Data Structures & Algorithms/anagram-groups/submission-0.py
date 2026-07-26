class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            sorted_strs = ''.join(sorted(i))
            if sorted_strs in seen:
                seen[sorted_strs].append(i)
            else:
                seen[sorted_strs] = [i]
        return list(seen.values())