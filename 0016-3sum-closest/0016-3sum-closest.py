class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = 2**31
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                for k in range(j,len(nums)):
                    if ((nums[i]+nums[j]+nums[k])-target) < ans:
                        ans = nums[i]+nums[j]+nums[k]
        return ans
        