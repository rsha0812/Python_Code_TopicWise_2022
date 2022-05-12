###Q) Write a function that takes an unsigned integer and returns the number of '1' bits it has.
'''
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.'''

### Soln : 
def hammingWeight(n: int) -> int:
        return bin(n).count("1")
print(hammingWeight(00000000001011))

'''
Qn: Given an integer number n, return the difference between the product of its digits and the sum of its digits.
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15 '''
### Soln: 
def subtractProductAndSum(n: int) -> int:
        sum = 0 
        mul = 1
        while n: 
            a = n%10 
            sum = sum + a 
            mul = mul * a
            n = n//10 
        return (mul-sum)
print(subtractProductAndSum(234)) ### 15

''' ---> Perimeter of Triangle : 
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. 
If it is impossible to form any triangle of a non-zero area, return 0.
Input: nums = [2,1,2]
Output: 5
Input: nums = [1,2,1]
Output: 0
'''
##### Soln: 
def largestPerimeter(nums):
        nums.sort()
      
        for i in range(len(nums)-3,-1,-1): ##012
            if nums[i] + nums[i+1] > nums[i+2]: 
                return nums[i] + nums[i+1] + nums[i+2]
                
        return 0
print(largestPerimeter([1,2,1])) ## 0 
print(largestPerimeter([2,1,2])) ## 5

''' ---- Two Sum Array: 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].'''
### Soln: 
def twosum(nums,target): 
    indx = {}
    for i in range(len(nums)): 
        result = target - nums[i]
        if result in indx: 
            return[i,indx[result]]
        indx[nums[i]] = i
    #return result 
print(twosum([2,7,11,15],9))


