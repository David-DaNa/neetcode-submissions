class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(0, len(nums)):
            remain = target - nums[i]
            if remain in seen:
                return [seen[remain], i]
            seen[nums[i]] = i
