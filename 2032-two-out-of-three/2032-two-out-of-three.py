class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)

        result = []

        for num in s1 | s2 | s3:
            if (num in s1) + (num in s2) + (num in s3) >= 2:
                result.append(num)

        return result