nums = [1, 3, 5, 6]
target = 5
# output should be 2

def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif nums[i] > target:
            return i
    return len(nums)

print(searchInsert(nums, target))