class Solution:
    @staticmethod
    def two_sum(some_nums: list[int], my_target: int) -> list[int]:
        for i in some_nums[:-1:]:
            for y in some_nums[some_nums.index(i) + 1:]:
                if i + y == my_target:
                    return [some_nums.index(i), some_nums.index(y)]


example = Solution()
nums = [2, 4]
target = 6
print(example.two_sum(nums, target))
print(nums[:-1:])
