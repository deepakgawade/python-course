



def partition(arr, low , high):
    pivot= arr[low]
    i=low
    j=high

    while i<j :
        while arr[i]<=pivot and i<=high-1:
            i+=1

        while arr[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            temp=0
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            #swap(arr[i], arr[j])
    temp=arr[low]
    arr[low]=arr[j]
    arr[j]=temp
    return j
    

def qs(arr, low , high):

    if low<high:
        partionIndex= partition(arr, low, high)

        qs(arr, low, partionIndex-1)
        qs(arr, partionIndex+1,high)

if __name__=="__main__":
    elements= [19,54,86,10,8,43]
   # elements= [5,4,3,2,1,0]
   # selection_sort(elements)
    #bubble_sort(elements)
    qs(elements, 0,len(elements)-1)
    print(elements)