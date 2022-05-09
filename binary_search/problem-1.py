

    # You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.

    # Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

    # We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

    # "Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].
from MySQLdb import Binary


class BinarySearch:

    def count_rotation(self,nums):
        n = len(nums)
        if n==0:
            return 0
        start =0
        end = n-1

        while start< end:
            mid= end +start//2

            prev=(mid-1+n)%n
            next =(mid+1)%n

            if nums[mid]<nums[prev] and nums[mid]<=nums[next]:
                return mid
            elif nums[mid]<nums[start]:end =mid-1
            elif nums[mid]>nums[end]:start=mid+1
            else: return 0

        pass 

    def count_rotations_linear(self,nums):
        position = 0 
    
        while position<len(nums):    
            if position > 0 and nums[position]<nums [position-1]: 
                return position
            position += 1
    
        return 0
    




if __name__=='__main__':
    test=[]
    # test case 1
    test0={
        "input":{
            "nums":[19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
        },
        "output":3
    
    }
    test.append(test0)
    #test case 2
    test1 = {
        'input': {
            'nums': [4,5,6,7,8,1,2,3]
        },
        'output': 5
    }
    test.append(test1)
    #test case 3
    test2 = {
        'input': {
            'nums': [1,2,3,4]
        },
        'output': 0
    }
    test.append(test2)
    #test case 4
    test3 = {
        'input': {
            'nums': [6,1,2,3,5]
        },
        'output': 1
    }
    test.append(test3)

    test4 = {
        'input': {
            'nums': [2,3,4,5,6,7,8,9,10,11,12,1]
        },
        'output': 11
    }
    test.append(test4)
    #test case 5
    test5 = {
        'input': {
            'nums':[1,2,3,4,5,6]
        },
        'output': 0
    }
    test.append(test5)
    #test case 6
    test6 = {
        'input': {
            'nums': []
        },
        'output': 0
    }
    test.append(test6)
    #test case 7
    test7 = {
        'input': {
            'nums': [2]
        },
        'output': 0
    }   
    test.append(test7)
    #check for all test cases
    search=BinarySearch()
    for t in test:
        num0=t["input"]["nums"]
        output0=t["output"]
        # result0=search.count_rotations_linear(num0)
        result0 =search.count_rotation(num0)
        if result0==output0:
            print("Test paased")
            print(result0)
        else:print("Test Failed")


   