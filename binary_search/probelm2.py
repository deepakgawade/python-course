# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.
#Answer:
# from hashlib import new


# class BinarySearch:
#     def find_target(self,arr,target):
#         n=len(arr)
#         newarry=[]
#         start=0
#         end=n-1
#         i=0
#        # notFound=false
#         while start<end:
#             if arr[i] == target:
#                 return i
#             elif target<arr[0]:
#                 arr.insert(0,target)
#                 return 0
#             elif target>arr[n-1]:
#                 arr.insert(n,target)
#                 return n
                
#             elif i<n-1:
#                 if target<arr[i] and target<arr[i+1]:
#                         arr.insert(i,target)
#                         return i
#             else:break
#             i=i+1
#     def find_byBinarySearch(self,arr,target):
#         n=len(arr)
#         start=0
#         end=n-1
    
#         if n<1:return 0
#         pos=0
#         while start<=end:
#             mid = (start+end)//2

#             if arr[mid]==target:
#                 return mid
#             elif target<arr[mid]:
#                 end=mid-1
#                 pos=mid
#             else:
#                 start=mid+1
#                 pos=mid+1
#         return pos
    
def binary_searh_iterative(arr,target):
    n= len(arr)
    low=0
    high=n-1


    while low <= high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1

    return -1

def binaryRecursive(arr, low, high,target):

    if low>=high:
        return
    
    mid= (low+high)//2

    if arr[mid]==target:
        return mid
    
    elif arr[mid] > target:
         binaryRecursive(arr,mid+1,high, target) 

    else:
        binaryRecursive(arr, low, mid-1, target)
    


if __name__=="__main__":
  

    test=[8,9,10,11,12,13,14,15,16]
    print("banga")
    print(binary_searh_iterative(test, 0))
    # test=[]
    # #first case
    # test0={"input":{
    #     "nums":[1,3,5,6],
    #     "target":5
    # },"output":2}
    # test.append(test0)
    # #second case
    # test1={"input":{
    #     "nums":[8,9,10,11,12,13,14,15,16],
    #     "target":14
    # },"output":6}
    # test.append(test1)
    # test2={"input":{
    #     "nums":[14],
    #     "target":14
    # },"output":0}
    # test.append(test2)
    # test3={"input":{
    #     "nums":[14],
    #     "target":15
    # },"output":1}
    # test.append(test3)
    # test4={"input":{
    #     "nums":[12],
    #     "target":4
    # },"output":0}
    # test.append(test4)
    # test5={"input":{
    #     "nums":[5,7,20,25],
    #     "target":3
    # },"output":0}
    # test.append(test5)
    # test6={"input":{
    #     "nums":[8,9,10,11,12,67,90,150,160],
    #     "target":91
    # },"output":7}
    # test.append(test6)
    # test7={"input":{
    #     "nums":[],
    #     "target":14
    # },"output":0}
    # test.append(test1)
    # for t in test:
    #     arr=t["input"]["nums"]
    #     target=t["input"]["target"]
    #     output=t["output"]
    #     inedx = search.find_byBinarySearch(arr,target)
    #     if inedx==output:
    #         print("Testt passed")
    #         print(inedx)
    #     else:print("test failed")
