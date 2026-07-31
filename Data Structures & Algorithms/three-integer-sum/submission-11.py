class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sorted_nums = sorted(nums)
        
        for i in range(len(nums)):
            l, r = i + 1, len(sorted_nums) - 1

            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            while l < r:
                total = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]

                if total == 0:
                    ans.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    r -= 1
                    l += 1

                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
                    
                    while l < r and sorted_nums[r] == sorted_nums[r + 1]:
                        r -= 1
                
                elif total > 0:
                    r -= 1
                
                else:
                    l += 1
        return ans