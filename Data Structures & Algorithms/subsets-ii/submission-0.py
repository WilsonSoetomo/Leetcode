class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(index, mini_list):
            if index == len(nums):
                res.append(mini_list[::])
                return 
            mini_list.append(nums[index])
            backtrack(index + 1, mini_list)
            mini_list.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                 index += 1
            backtrack(index + 1, mini_list)

        backtrack(0, [])

        return res
