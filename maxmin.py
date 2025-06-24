# Maxmin.py
def maxmin(nums):
    """Takes in a list of int, returns the minimum, maximum in the format: [min,max]"""
    if not nums:
        return [0, 0]
    nums = sorted(nums)
    return [nums[0], nums[-1]]


print(maxmin([2, 4, 1, 0, 2, -1]))
print(maxmin([20, 50, 12, 6, 14, 8]))
print(maxmin([100, -100]))
