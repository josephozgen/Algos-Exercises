def twoSum(nums, target: int):
    dct = {}
    for i, num in enumerate(nums):
        if target-num in dct:
            return [dct[target-num], i]
        dct[num] = i
    return "It nevere reaches out this line..."

print(twoSum([3,5,7,11,15],26))