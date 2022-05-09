# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.
#Answer:
from hashlib import new
from sqlalchemy import false, true


class BinarySearch:
    def find_target(self,arr,target):
        n=len(arr)
        newarry=[]
        start=0
        end=n-1
        i=0
        notFound=false
        while start<end:
            if arr[i] == target:
                return i
            elif target<arr[i] or target>arr[i+1]:
                arr.insert(i,target)
                return i
            i=i+1

if __name__=='__main__':
    search = BinarySearch()
    arr=[2,4,5,78,96,100]
    inedx = search.find_target(arr,1)
    print(inedx)
