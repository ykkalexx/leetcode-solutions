nums= [1,2,3,1]

# Time complexity: O(n^2)
def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1 ,len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

print(containsDuplicate(nums))

# Time complexity: O(n)
def containsDuplicates(nums):
    if len(set(nums)) == len(nums):
        return False
    
    return True

print(containsDuplicate(nums))