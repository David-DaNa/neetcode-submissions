class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # sorted_nums = sorted(nums)
        # longest = 1
        # current = 1
        # for i in range(1, len(sorted_nums)):
        #     if sorted_nums[i] == sorted_nums[i - 1]:
        #         continue
        #     if sorted_nums[i] == sorted_nums[i - 1] + 1:
        #         current += 1
        #     else:
        #         current = 1
            
        #     longest = max(longest, current)

        # return longest
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                length = 1

                while num + length in nums_set:
                    length += 1

                longest = max(longest, length)

        return longest