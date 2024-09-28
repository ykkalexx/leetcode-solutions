nums = [2,2,1]
#output = 1

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


print(singleNumber(nums))