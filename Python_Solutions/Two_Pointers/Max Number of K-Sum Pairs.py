class Solution:
    def maxOperations(self, nums, k: int):
        for idx, num in enumerate(nums):
            nums.sort()
            i, j = 0, len(nums) - 1
            cont = 0
            while i<j:
                summ = nums[i]+nums[j]
                if summ == k:
                    i+=1
                    j-=1
                    cont+=1
                elif summ>k:
                    j-=1
                else:
                    i+=1

            return cont

            