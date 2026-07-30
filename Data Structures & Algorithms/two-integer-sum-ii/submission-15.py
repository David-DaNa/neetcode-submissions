class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left = 0
        # while left < len(numbers) - 1:
        #     right = 1
        #     while right < len(numbers):
        #         for i in range(len(numbers)):
        #             if numbers[left] == target - numbers[right]:
        #                 return [left + 1, right + 1] 
        #         right += 1
        #     left += 1
        l, r = 0, len(numbers) - 1
        while l < r:
            current = numbers[l] + numbers[r]
            if current > target:
                r -= 1
            elif current < target:
                l += 1
            else:
                return [l+1, r+1]