def bubble_sort(arr, n):
    if n==1:
        print(arr)
        return
    temp=0
    for j in range(n-1):
     
        if arr[j]>arr[j+1]:
            temp= arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
    
    bubble_sort(arr, n-1)

if __name__== "__main__":

      elements= [19,54,86,10,8,43]
      bubble_sort(elements, len(elements))
      
        