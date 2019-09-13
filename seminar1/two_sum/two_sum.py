from bisect import bisect_left


def contains(nums, x):
    index = bisect_left(nums, x)
    if index < len(nums) and nums[index] == x:
        return index
    return -1

def two_sum_with_one_solution(nums, target):
    sorted_nums = sorted(nums)
    ans = False
    for i, n in enumerate(sorted_nums):
        pair_index = contains(sorted_nums, target - n)
        if pair_index != -1 and i != pair_index:
            ans = [i, pair_index]
            break
    if ans != False:
        ans = [
                nums.index(sorted_nums[ans[0]]), 
                nums.index(sorted_nums[ans[1]])
                ]
    return ans

def two_sum_with_repetition(nums, target):
    sorted_nums = sorted(nums)
    ans = False
    for i, n in enumerate(sorted_nums):
        pair_index = contains(sorted_nums, target - n)
        if pair_index != -1:
            ans = [i, pair_index]
            break
    if ans != False:
        ans = [
                nums.index(sorted_nums[ans[0]]), 
                nums.index(sorted_nums[ans[1]])
                ]
    return ans

