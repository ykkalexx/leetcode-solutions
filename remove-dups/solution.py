nums = [0,0,1,1,1,2,2,3,3,4]
# output length = 5 (0, 1, 2, 3, 4) and add _ to the replaiced numbers

def removeDuplicates(nums):
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return k
        
print(removeDuplicates(nums))