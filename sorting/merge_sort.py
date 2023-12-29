def ms(arr, low , high):
    if (low==high): return

    mid= (low+high)//2

    ms(arr, low,mid)
    ms(arr, mid+1, high)
    merge(arr, low ,mid, high)



    

def merge(arr, low, mid, high):
    temp=[]
    left=low
    right=mid+1
    
    print(f"arr before merge: {arr}")
    while(left<=mid and right<=high):
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1

    while(left<=mid):
        temp.append(arr[left])
        left+=1

    while(right<=high):
        temp.append(arr[right])
        right+=1

    print(f"temp: {temp}")

    for i in range(low,high+1):
        print(f"i :{i} low:{low} high: {high}")
      
        arr[i]=temp[i-low]
    print(f"arr: {arr}")

# timecomplexity is O(logn)

   
    

def merge_sort(arr, n):
    ms(arr, 0, n-1)
    print(f"second smallest :{arr[1]}\n second largest{arr[n-2]}")
   # print(elements)

if __name__=="__main__":
    elements= [19,54,86,10,8,43]
   # elements= [5,4,3,2,1,0]
   # selection_sort(elements)
    #bubble_sort(elements)
    merge_sort(elements, len(elements))
    print(elements)
