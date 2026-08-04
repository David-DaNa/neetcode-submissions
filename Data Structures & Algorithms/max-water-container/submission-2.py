class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        ans = 0

        while start < end:
            width = end - start
            temp = min(heights[start], heights[end]) * width

            if temp > ans:
                ans = temp

            if heights[start] > heights[end]:
                end -= 1

            elif heights[start] <= heights[end]:
                start += 1
        return ans
            