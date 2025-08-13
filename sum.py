def sum_of_three_numbers(nums):
    nums.sort()
    product1=nums[-1]+nums[-2]+nums[-3]
    product2=nums[0]+nums[1]+nums[-1]
    return product1,product2
nums=[-3, -1, 2, 3, 4]
print(sum_of_three_numbers(nums))
