class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute Force
        # ans = [0] * len(nums)
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         product *= nums[j]
        #     ans[i] = product
        # return ans
        
        # Prefix, Postfix using 3 arrays
        # n = len(nums)
        # pref = [0] * n
        # suff = [0] * n
        # res = [0] * n

        # pref[0] = 1
        # suff[n - 1] = 1
        # for i in range(1, n):
        #     pref[i] = nums[i - 1] * pref[i - 1]
        # for i in range(n - 2, -1, -1):
        #     suff[i] = nums[i + 1] * suff[i + 1]
        # for i in range(n):
        #     res[i] = pref[i] * suff[i]
        # return res

        # Prefix, Postfix 1 array
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
