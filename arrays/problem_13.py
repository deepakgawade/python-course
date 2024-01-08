

#we can use merge sort which will have O(log n)
# def sortArray012(arr):
#     n=len(arr)
#     left=0
#     right=1
#     temp=0
#     for i in range()

#         if arr[left]<=arr[right]:
#             left+=1
#         else:
#             temp=arr[left]
#             arr[left]=arr[right]
#             arr[right]=temp
#             right+=1
     

#     print(arr)

#variation of Dutch flag algorithm

def sortArray012(arr):
    n=len(arr)
    mid=0
    low=0 
    high=n-1

    while mid<=high:
        if arr[mid]==0:
            arr[low], arr[mid]= arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[high],arr[mid]=arr[mid],arr[high]
            high-=1

    print(arr)


#time complexity O(N)
#space complexity O(1) 


if __name__=="__main__":
    elements=[2,0,2,1,1,0]
    sortArray012(elements)

            



    