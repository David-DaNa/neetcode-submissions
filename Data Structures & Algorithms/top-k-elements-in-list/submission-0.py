class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        sorted_seen = sorted(seen.items(), key=lambda x: x[1], reverse=True)
        ans = []
        for j in range(k):
            ans.append(sorted_seen[j][0])
        return ans
