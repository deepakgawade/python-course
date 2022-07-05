# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# test cases 1: nums= [3,0,1] num.length=3  gen_num=0[0,1,2,3] check for num in the list missing number.
#
#N=int(input())



class Solution:
    def missingNumber(self, nums):
        for j in range(len(nums)):
            if j not in nums:
                return j
        return len(nums)

if __name__=="__main__":
    n=input()
    search= Solution()
    arr= list(map(int , input().split(',')))
    vum=search.missingNumber(arr)
    print(vum)
